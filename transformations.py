from MongoDB_API import MongoDBAPI

def transform_field_to_integer(collection, field_name):
    # Loop through docs in collection
    for document in collection.find():
        # Check if specified field exists in doc
        if field_name in document:
            # Get original value of field
            original_value = document[field_name]

            try:
                # Remove commas and convert into integer
                new_value = int(str(original_value).replace(',', ''))
                # Update doc with new int value
                collection.update_one({"_id": document["_id"]}, {"$set": {field_name: new_value}})
            except ValueError:
                # Handle commas and strange things
                pass

def perform_transformations():
    # Create a MongoDBAPI instance
    mongodb_api = MongoDBAPI()

    # Specify database and collection names
    database_name = 'starwars'
    collection_name = 'starships'

    # Connect to "starships" collection
    starships_collection = mongodb_api.connect_to_mongo(database_name)[collection_name]

    # List fields for transformation
    fields_to_transform = ['crew', 'cargo_capacity', 'passengers', 'cost_in_credits', 'length', 'max_atmosphering_speed']

    # Transform specified fields to integers
    for field in fields_to_transform:
        transform_field_to_integer(starships_collection, field)

if __name__ == "__main__":
    # Perform transformations
    perform_transformations()
