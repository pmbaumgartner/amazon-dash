from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://dog:dash@ds139425.mlab.com:39425/dog-dash")

db = client['dog-dash']

coll = db['records_collection']

coll.insert_one(
    {
        'dog': 'Ellis',
        'time': datetime.datetime.now()
    }
)

print(coll.count())
