import json
import requests
import pymongo

client = pymongo.MongoClient()
db = client['StarWars']

starships = []

#Calling Api
for i in range(76):
    link = "https://swapi.dev/api/starships/"+str(i)
    my_json = requests.get(link).json()
    if (my_json != {'detail': 'Not found'}):
        starships.append(my_json)

# CAlling name API
for ship in starships:
    pilots = []
    for pilot in ship["pilots"]:
        pilot_name = requests.get(pilot).json()["name"]

        # Finding the ID
        pilots.append(db.characters.find({"name":pilot_name},{"_id":1}))

    # Replacing starship pilot field
    for pilot in pilots:
        ship["pilots"] = [x["_id"] for x in pilot]

# Adding into the database
collection = db["Starships"]
for ship in starships:
    result = collection.insert_one(ship)