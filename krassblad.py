import pymongo
import requests


def replace_field_old(database_name, collection_A, collection_B, field_A, field_B, replacement="_id"):
    collection_A = connect_to_mongo(database_name)[collection_A]
    collection_B = connect_to_mongo(database_name)[collection_B]

    for document in collection_A:
        if field_A in document:
            for element in field_A:
                # Search for a name in the other collection, and return it's replacement
                result = collection_B.find({field_B: element}, {replacement: 1})
                for inner_element in result:
                    collection_A.update_one({"_id": document["_id"]}, {"$set": {field_A: inner_element[replacement]}})

def replace_field(database_name, collection_A, collection_B, field_A, field_B, replacement="_id"):
    collection_A = connect_to_mongo(database_name)[collection_A]
    collection_B = connect_to_mongo(database_name)[collection_B]

    for document in collection_A.find():
        print(document)

replace_field("StarWars",'Starships',"characters","pilots","name")