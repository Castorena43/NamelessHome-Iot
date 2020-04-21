import pymongo

class Mongo():

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://house174:esuoh174@uttics.com:27027/?authSource=house&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
        self.database = self.client['house']

    def getData(self,cuarto,feed):
        c1 = self.database[cuarto]
        r = c1.find_one({'feed':feed})
        return r['value']
