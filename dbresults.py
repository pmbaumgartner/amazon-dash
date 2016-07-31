from pymongo import MongoClient
import arrow

client = MongoClient("mongodb://dog:dash@ds139425.mlab.com:39425/dog-dash")

db = client['dog-dash']

coll = db['records_collection']

miles_poo = coll.find_one({'dog' : 'Miles', 'outcome' : 'poop'}, sort=[('time', -1)])
ellis_poo = coll.find_one({'dog' : 'Ellis', 'outcome' : 'poop'}, sort=[('time', -1)])
miles_pee = coll.find_one({'dog' : 'Miles', 'outcome' : 'pee'}, sort=[('time', -1)])
ellis_pee = coll.find_one({'dog' : 'Ellis', 'outcome' : 'pee'}, sort=[('time', -1)])

print("Miles Poop:", arrow.get(miles_poo['time']).humanize())
print("Miles Pee:", arrow.get(miles_pee['time']).humanize())
print("Ellis Poop:", arrow.get(ellis_poo['time']).humanize())
print("Ellis Pee:", arrow.get(ellis_pee['time']).humanize())
