import pymongo


# class which interacts with MongoDB
class MongoDBAPI:
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
                    # Search for a name in the other collection, and return it's replacement
                    result = collection_to_retrieve.find({field_to_find: element}, {replacement_field: 1})
                    # Grab the replacement field (by default the ID)
                    for inner_element in result:
                        field_to_update.append(inner_element[replacement_field])
                # Set the field to replace, with the replacement field
                collection_to_replace.update_one({"_id": document["_id"]},
                                                 {"$set": {field_to_replace: field_to_update}})

    def create_collection(self, database_name, collection_name):
        return self.connect_to_mongo(database_name)[collection_name]

    def insert_lst_into_db(self, lst, collection):
        collection.insert_many(lst)
