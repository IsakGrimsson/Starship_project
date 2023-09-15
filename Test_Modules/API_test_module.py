import unittest
from API_pymongo import StarWarsAPI
import pymongo

class UnitTests_StarWarsAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.StarWarsAPI = StarWarsAPI()
    def test_fetch_page(self):
        json_collection = self.StarWarsAPI.fetch_page('starships', 1)
        actual = len(json_collection[0])
        expected = 18
        self.assertEqual(actual, expected, 'expected length of Json file has been met')

    def test_fetch_indexed_value(self):
        json_collection = self.StarWarsAPI.fetch_page('starships', 1)
        actual = json_collection[3]['name']
        expected = "Death Star"
        self.assertEqual(actual, expected, 'the death star is built and ready')

    def test_num_of_pages(self):
        client = pymongo.MongoClient()
        db = client['StarWars']
        json_numbers = self.StarWarsAPI.fetch_num_pages('starships', 2)
        actual = len(json_numbers)
        expected = 20


# sw = StarWarsAPI()
# json_collection = sw.fetch_page('starships', 1)
# print(json_collection[3]['name'])
# for starship in Starships:
#     print(starship)
# sw = StarWarsAPI()
# json_numbers = sw.fetch_num_pages('starships', 4)
# print(json_numbers.count)
# sw = StarWarsAPI()
# json_numbers = sw.fetch_num_pages('starships', 2)
# print(len(json_numbers))