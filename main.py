from StarWars_API import StarWarsAPI
from MongoDB_API import MongoDBAPI
from transformations import transform_field_to_integer

sw = StarWarsAPI()
mg = MongoDBAPI()

# Fetch the data
starships_data = sw.fetch_all_pages("starships")

# Manipulate it by replacing the LINKS with NAMES
new_starships_data = sw.replace_url(starships_data, 'pilots', 'name')

# Perform transformations
transform_field_to_integer(new_starships_data, 'crew')
transform_field_to_integer(new_starships_data, 'cargo_capacity')
transform_field_to_integer(new_starships_data, 'passengers')
transform_field_to_integer(new_starships_data, 'cost_in_credits')
transform_field_to_integer(new_starships_data, 'length')
transform_field_to_integer(new_starships_data, 'max_atmosphering_speed')

# Insert into database
collection = mg.create_collection('starwars', 'starships')
mg.insert_lst_into_db(new_starships_data, collection)

# Manipulate by replacing NAMES with ID
mg.replace_field("starwars", 'starships', "pilots", "characters", "name")
