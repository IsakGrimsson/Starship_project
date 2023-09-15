from API_pymongo import StarWarsAPI
from API_pymongo import MongoDB
import pymongo
import requests


sw = StarWarsAPI()
mg = MongoDB()
starships_data = sw.fetch_all_pages("starships")

new_starships_data = mg.replace_inner_url(starships_data, 'pilots')

mg.insert_data(new_starships_data, 'starwars', 'starships')




