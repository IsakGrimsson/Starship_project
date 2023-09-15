from StarWars_API import StarWarsAPI
from MongoDB_API import MongoDBAPI
sw = StarWarsAPI()
mg = MongoDBAPI()

# Fetch the data
starships_data = sw.fetch_all_pages("starships")
# Manipulate it by replacing the LINKS with the NAMES
new_starships_data = sw.replace_url(starships_data, 'pilots', 'name')
# Insert it into the database
mg.insert_data(new_starships_data, 'StarWars', 'Starships')
# Manipulate it by replacing the NAMES with the ID
mg.replace_field("StarWars", 'Starships', "pilots", "characters", "name")

