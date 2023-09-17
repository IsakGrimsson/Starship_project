from StarWars_API import StarWarsAPI
from MongoDB_API import MongoDBAPI
from transformations import Transformations

sw = StarWarsAPI()
mg = MongoDBAPI()
tr = Transformations()

# Fetch the data
starships_data = sw.fetch_all_pages("starships")

# Manipulate it by replacing the LINKS with NAMES
new_starships_data = sw.replace_url(starships_data, 'pilots', 'name')

# Perform transformations
tr.clean_unknown(new_starships_data, 'consumables')
tr.clean_unknown(new_starships_data, 'hyperdrive_rating')
tr.clean_unknown(new_starships_data, 'cost_in_credits')
tr.clean_unknown(new_starships_data, 'cargo_capacity')
tr.clean_unknown(new_starships_data, 'MGLT')
tr.clean_unknown(new_starships_data, 'passengers')
tr.clean_unknown(new_starships_data, 'crew')
tr.clean_unknown(new_starships_data, 'max_atmosphering_speed')

tr.clean_na(new_starships_data, 'max_atmosphering_speed')
tr.clean_na(new_starships_data, 'passengers')

tr.normalise_data(new_starships_data, 'name')
tr.normalise_data(new_starships_data, 'model')
tr.normalise_data(new_starships_data, 'manufacturer')
tr.normalise_data(new_starships_data, 'starship_class')

tr.transform_field_to_float(new_starships_data, 'length')
tr.transform_field_to_float(new_starships_data, 'hyperdrive_rating')

tr.transform_field_to_integer(new_starships_data, 'crew')
tr.transform_field_to_integer(new_starships_data, 'cargo_capacity')
tr.transform_field_to_integer(new_starships_data, 'passengers')
tr.transform_field_to_integer(new_starships_data, 'cost_in_credits')
tr.transform_field_to_integer(new_starships_data, 'max_atmosphering_speed')
tr.transform_field_to_integer(new_starships_data, 'MGLT')

# Insert into database
collection = mg.create_collection('starwars', 'starships')
mg.insert_lst_into_db(new_starships_data, collection)

# Manipulate by replacing NAMES with ID
mg.replace_field("starwars", 'starships', "pilots", "characters", "name")
