import unittest
from MongoDB_API import MongoDBAPI


class TestAPIMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.MongoDB = MongoDBAPI()
    def test_insert_data(self):
        collection = self.MongoDB.create_collection("testdb", "test_collection")
        self.assertIsNotNone(collection)

    def test_insert_into_collection(self):
        collection = self.MongoDB.create_collection("testdb", "test_collection")
        self.MongoDB.insert_lst_into_db([{'1': 'one'}, {'2': 'two'}, {'3': 'three'}, {'4': 'four'}], collection)
        actual = collection.count_documents({})
        expected = 4
        self.assertEqual(actual, expected)

    def test_mongo_connection(self):
        connection = self.MongoDB.connect_to_mongo('testdb')
        self.assertIsNotNone(connection)
