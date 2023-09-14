import requests
import pymongo

def get_starships():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["starwars"]
    pages = [1,2,3,4]
    for n in pages:
        starships = requests.get(f"https://swapi.dev/api/starships/?page={n}&page1=")
        starships_data = starships.json()["results"]
        starships_collection = db["starships"]
        starships_collection.insert_many(starships_data)

get_starships()