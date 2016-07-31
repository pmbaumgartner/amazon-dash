from scapy.all import *
from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://dog:dash@ds139425.mlab.com:39425/dog-dash")

db = client['dog-dash']

coll = db['records_collection']

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].hwsrc == '44:65:0d:a6:17:55': #plum Organics
        coll.insert_one(
            {
                'dog': 'BUTTON',
                'time': datetime.datetime.now()
            }
        )
      print ("Plum Organics detected")

sniff(prn=arp_display, filter="arp", store=0, count=0)
