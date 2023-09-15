import unittest
from API_pymongo import StarWarsAPI

class UnitTests_StarWarsAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.StarWarsAPI = StarWarsAPI()
    def test_fetch_page(self):
        self.StarWarsAPI.fetch_page('starships', 2)


