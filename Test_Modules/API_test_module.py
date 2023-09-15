import unittest
from StarWars_API import StarWarsAPI
import pymongo
import requests

class UnitTests_StarWarsAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.StarWarsAPI = StarWarsAPI()
    def test_fetch_document_length(self):
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
        json_numbers = self.StarWarsAPI.fetch_num_pages('starships', 3)
        actual = len(json_numbers)
        expected = 30
        self.assertEqual(actual, expected, 'The number of documents in each page is correct')

    def test_fetch_all_pages(self):
        count_request = requests.get("https://swapi.dev/api/starships")
        expected = count_request.json()["count"]
        json_collection = self.StarWarsAPI.fetch_all_pages('starships')
        actual = len(json_collection)
        self.assertEqual(actual, expected, 'The number of starships is equal to that seen on the API website')
