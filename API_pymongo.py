import pymongo
import requests


class StarWarsAPI:
    def fetch_page(self, collection: str, page: int):
        page_request = requests.get(f"https://swapi.dev/api/{collection}/?page={page}")
        return page_request.json()["results"]

    def fetch_many_pages(self, collection: str, num_of_pages: int):
        all_pages = []
        for page in list(range(1,num_of_pages+1)):
            each_page = self.fetch_page(collection, page)
            all_pages.extend(each_page)
        return all_pages

class MongoDB:
    def __init__(self):
        self.default_server = "mongodb://localhost:27017/"

    def connect_to_mongo(self, db: str, server: str = "mongodb://localhost:27017/"):
        client = pymongo.MongoClient(server)
        database = client[db]
        return database

    def insert_data(self, lst, database_name, collection_name):
        data_collection = self.connect_to_mongo(database_name)[collection_name]
        data_collection.insert_many(lst)



