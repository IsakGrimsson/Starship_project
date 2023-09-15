import unittest
from API_pymongo import MongoDB


class TestAPIMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.MongoDB = MongoDB()
    def test_insert_data(self):
        data_collection = self.MongoDB.insert_data([1, 2, 3, 4], "testdb", "test_collection")
        self.assertIsNotNone(data_collection)