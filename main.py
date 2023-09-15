from StarWars_API import StarWarsAPI
from MongoDB_API import MongoDBAPI
sw = StarWarsAPI()
mg = MongoDBAPI()

# Fetch the data
starships_data = sw.fetch_all_pages("starships")

# Manipulate it by replacing the LINKS with the NAMES
new_starships_data = sw.replace_url(starships_data, 'pilots', 'name')

# Insert it into the database
collection = mg.create_collection('starwars', 'starships')
mg.insert_lst_into_db(new_starships_data, collection)

# Manipulate it by replacing the NAMES with the ID
mg.replace_field("starwars", 'starships', "pilots", "characters", "name")

