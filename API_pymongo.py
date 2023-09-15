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

    def replace_url(self, list_of_dicts, inner, retrieve):
        for dict in list_of_dicts:
            url_replaced_with_retrieve = []
            for url in dict[inner]:
                url_json = requests.session().get(url).json()
                retrieve_element = url_json[retrieve]
                url_replaced_with_retrieve.append(retrieve_element)
            dict[inner] = url_replaced_with_retrieve
        return list_of_dicts

#class which interacts with MongoDB
class MongoDB:
    def __init__(self):
        self.default_server = "mongodb://localhost:27017/"

    def connect_to_mongo(self, db: str, server: str = "mongodb://localhost:27017/"):
        client = pymongo.MongoClient(server)
        database = client[db]
        return database

    def replace_field(self, database_name,
                      collection_to_replace, field_to_replace,
                      collection_to_retrieve, field_to_find, replacement_field="_id"):

        # Establish connections
        collection_to_replace = self.connect_to_mongo(database_name)[collection_to_replace]
        collection_to_retrieve = self.connect_to_mongo(database_name)[collection_to_retrieve]

        # Replacement each field, with its replacement
        # For each document in the collection to replace
        for document in collection_to_replace.find():
            # If the field exists
            if field_to_replace in document:
                field_to_update = []
                # For each element in the field to replace
                for element in document[field_to_replace]:
                    #Search for a name in the other collection, and return it's replacement
                    result = collection_to_retrieve.find({field_to_find:element}, {replacement_field:1})
                    # Grab the replacement field (by default the ID)
                    for inner_element in result:
                        field_to_update.append(inner_element[replacement_field])
                # Set the field to replace, with the replacement field
                collection_to_replace.update_one({"_id": document["_id"]}, {"$set": {field_to_replace:field_to_update}})




    def insert_data(self, lst, database_name, collection_name):
        data_collection = self.connect_to_mongo(database_name)[collection_name]
        data_collection.insert_many(lst)



