from API_pymongo import StarWarsAPI
from API_pymongo import MongoDB
import pymongo
import requests


sw = StarWarsAPI()
mg = MongoDB()
starships_data = sw.fetch_all_pages("starships")


new_starships_data = sw.replace_url(starships_data, 'pilots', 'name')
mg.insert_data(new_starships_data, 'StarWars', 'Starships')

mg.replace_field("StarWars",'Starships',"characters","pilots","name")

