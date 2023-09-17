from MongoDB_API import MongoDBAPI

# Transforms numeric string fields to integers.
def transform_field_to_integer(data_list, field_name):
    for item in data_list:
        if field_name in item:
            original_value = item[field_name]
            try:
                new_value = int(str(original_value).replace(',', ''))
                item[field_name] = new_value
            except ValueError:
                pass

# Transforms numeric string fields to double.
def transform_field_to_float(data_list, field_name):
    for item in data_list:
        if field_name in item:
            original_value = item[field_name]
            try:
                new_value = float(str(original_value).replace(',', ''))
                item[field_name] = new_value
            except ValueError:
                pass

# Cleaning unknown value in empty string.
def clean_unknown(data_list, field_name):
    for item in data_list:
        if field_name in item:
            original_value = item[field_name]
            try:
                new_value = str(original_value).replace('unknown', '')
                item[field_name] = new_value
            except ValueError:
                pass

# Cleaning n/a value in empty string.
def clean_na(data_list, field_name):
    for item in data_list:
        if field_name in item:
            original_value = item[field_name]
            try:
                new_value = str(original_value).replace('n/a', '')
                item[field_name] = new_value
            except ValueError:
                pass

# Normalising the data by capitalising each first letter of a string.
def normalise_data(data_list, field_name):
    for item in data_list:
        if field_name in item:
            original_value = item[field_name]
            try:
                new_value = str(original_value).replace(',', '').title()
                item[field_name] = new_value
            except ValueError:
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
    fields_to_transform = ['crew',
                           'cargo_capacity',
                           'passengers',
                           'cost_in_credits',
                           'length',
                           'max_atmosphering_speed',
                           'MGLT',
                           'consumables',
                           'hyperdrive_rating',
                           'name',
                           'model',
                           'manufacturer',
                           'starship_class']

    for field in fields_to_transform:
        clean_unknown(starships_collection, field)

    for field in fields_to_transform:
        clean_na(starships_collection, field)

    for field in fields_to_transform:
        transform_field_to_float(starships_collection, field)

    for field in fields_to_transform:
        normalise_data(starships_collection, field)
    # Transform specified fields to integers
    for field in fields_to_transform:
        transform_field_to_integer(starships_collection, field)


if __name__ == "__main__":
    # Perform transformations
    perform_transformations()
