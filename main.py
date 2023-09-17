from StarWars_API import StarWarsAPI
from MongoDB_API import MongoDBAPI
from transformations import transform_field_to_integer, clean_unknown, transform_field_to_float, clean_na, normalise_data

sw = StarWarsAPI()
mg = MongoDBAPI()

# Fetch the data
starships_data = sw.fetch_all_pages("starships")

# Manipulate it by replacing the LINKS with NAMES
new_starships_data = sw.replace_url(starships_data, 'pilots', 'name')

# Perform transformations
clean_unknown(new_starships_data, 'consumables')
clean_unknown(new_starships_data, 'hyperdrive_rating')
clean_unknown(new_starships_data, 'cost_in_credits')
clean_unknown(new_starships_data, 'cargo_capacity')
clean_unknown(new_starships_data, 'MGLT')
clean_unknown(new_starships_data, 'passengers')
clean_unknown(new_starships_data, 'crew')
clean_unknown(new_starships_data, 'max_atmosphering_speed')

clean_na(new_starships_data, 'max_atmosphering_speed')
clean_na(new_starships_data, 'passengers')

normalise_data(new_starships_data, 'name')
normalise_data(new_starships_data, 'model')
normalise_data(new_starships_data, 'manufacturer')
normalise_data(new_starships_data, 'starship_class')

transform_field_to_float(new_starships_data, 'length')
transform_field_to_float(new_starships_data, 'hyperdrive_rating')

transform_field_to_integer(new_starships_data, 'crew')
transform_field_to_integer(new_starships_data, 'cargo_capacity')
transform_field_to_integer(new_starships_data, 'passengers')
transform_field_to_integer(new_starships_data, 'cost_in_credits')
transform_field_to_integer(new_starships_data, 'max_atmosphering_speed')
transform_field_to_integer(new_starships_data, 'MGLT')

# Insert into database
collection = mg.create_collection('starwars', 'starships')
mg.insert_lst_into_db(new_starships_data, collection)

# Manipulate by replacing NAMES with ID
mg.replace_field("starwars", 'starships', "pilots", "characters", "name")
