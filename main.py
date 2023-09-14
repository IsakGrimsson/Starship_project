from API_pymongo import StarWarsAPI
from API_pymongo import MongoDB

sw = StarWarsAPI()
mg = MongoDB()
starships_data = sw.fetch_many_pages("starships", 4)

mg.insert_data(starships_data, 'starwars', 'starships')



