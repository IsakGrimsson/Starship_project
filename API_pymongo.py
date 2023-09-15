import pymongo
import requests


#class to fetch data from API and return array of dictionaries
class StarWarsAPI:
    #fetch one specific page number
    def fetch_page(self, collection: str, page: int):
        page_request = requests.session().get(f"https://swapi.dev/api/{collection}/?page={page}")
        return page_request.json()["results"]
    #fetch the first x number of pages
    def fetch_num_pages(self, collection: str, num_of_pages: int):
        all_pages = []
        for page in list(range(1,num_of_pages+1)):
            each_page = self.fetch_page(collection, page)
            all_pages.extend(each_page)
        return
    #fetch all of the pages for specified collection
    def fetch_all_pages(self, collection: str):
        all_pages = []
        page = 1
        while True:
            page_request = requests.get(f"https://swapi.dev/api/{collection}/?page={page}")
            # added .get so that when there is no response it will recover
            page_data = page_request.json().get("results", [])
            # break when there is no more data
            if not page_data:
                break
            all_pages.extend(page_data)
            page += 1
        return all_pages

#class which interacts with MongoDB
class MongoDB:
    def __init__(self):
        self.default_server = "mongodb://localhost:27017/"

    def connect_to_mongo(self, db: str, server: str = "mongodb://localhost:27017/"):
        client = pymongo.MongoClient(server)
        database = client[db]
        return database
    def replace_inner_url(self, list_of_dicts, inner):
        for dict in list_of_dicts:
            inner_elements = []
            # For each inner element on each outer element
            for inn in dict[inner]:
                # make a request to the API to grab their name
                inner_name = requests.session().get(inn).json()['name']
                # Search the DB by name to find their ID and add them to the pilots array
                inner_element = self.connect_to_mongo('starwars').characters.find({"name": inner_name}, {"_id": 1})
                for document in inner_element:
                    inner_elements.append(document["_id"])
                # Replace the "pilots" field (for each ship)
            dict["pilots"] = inner_elements
        return list_of_dicts
    def insert_data(self, lst, database_name, collection_name):
        data_collection = self.connect_to_mongo(database_name)[collection_name]
        data_collection.insert_many(lst)



