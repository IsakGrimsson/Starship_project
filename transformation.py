import pymongo


class StarshipsTransformation:
    def __init__(self, db, collection):
        self.client = pymongo.MongoClient()
        self.db = self.client['starwars']
        self.collection = self.db['starships']

    def data(self):
        starships = self.collection.find({})
        for starship in starships:
            print(starship)


    def convert_numerical_fields(self):
        starships = self.collection.find({})
        for starship in starships:
            starship.update_one({
                "cost_in_credits",
                "length","max_atmosphering_speed"},
                {"$set": {
                "cost_in_credits": int(starships["cost_in_credits"]),
                "length": float(starships["length"]),
                "max_atmosphering_speed": int(starships["max_atmosphering_speed"]),
                "crew": int(starships["crew"]),
                "passengers": int(starships["passengers"]),
                "cargo_capacity": int(starships["cargo_capacity"]),
                "hyperdrive_rating": float(starships["hyperdrive_rating"]),
            }})
            print(starship)

    def handle_missing_values(self):
        self.collection.update_one({}, {"$unset": {"MGLT": ""}})
        print(self.collection)
    #
    # {"mass": "1,358"},
    # {"$set": {"mass": "1358"}}




# class ConvertNumericalFields(StarshipsTransformation):
#     def cost_in_credits(self):
#         starships = self.collection.find({})
#         for starship in starships:
#             starship.update_many({"cost_in_credits"},
#                                  {"$set": int(starships["cost_in_credits"])}}
#


            # Create an instance of the class
transformation = StarshipsTransformation('starwars', 'starships')

            # Call the data method on the instance
transformation.handle_missing_values()