import json
import requests
import pymongo

client = pymongo.MongoClient()
db = client['StarWars']

starships = []

# Calling Api to gather all the starships
for i in range(20):
    link = "https://swapi.dev/api/starships/"+str(i)
    my_json = requests.get(link).json()
    if (my_json != {'detail': 'Not found'}):
        starships.append(my_json)

# Format the starships array with the objectID instead of the API link
for ship in starships:
    pilots = []
    # For each pilot on each ship
    for pilot in ship["pilots"]:
        # make a request to the API to grab their name
        pilot_name = requests.get(pilot).json()["name"]
        # Search the DB by name to find their ID and add them to the pilots array
        pilot = db.characters.find({"name":pilot_name},{"_id":1})
        for document in pilot:
            pilots.append(document["_id"])

    # Replace the "pilots" field (for each ship)
    ship["pilots"] = pilots

# Adding into the database
collection = db["Starships"]
for ship in starships:
    result = collection.insert_one(ship)