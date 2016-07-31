from scapy.all import *
from pymongo import MongoClient
import datetime

from time import sleep, time

client = MongoClient("mongodb://dog:dash@ds139425.mlab.com:39425/dog-dash")

db = client['dog-dash']

coll = db['records_collection']

def arp_display(pkt):
    capture_time = time()
    if pkt[ARP].op == 1:
        if pkt[ARP].hwsrc == '44:65:0d:a6:17:55':
            if time() - capture_time > 3:
                time_now = datetime.datetime.now() # plum Organics
                coll.insert_one(
                    {
                        'dog': 'BUTTON',
                        'time': time_now
                    }
                )
                print("Plum Organics detected")

                capture_time = time()

sniff(prn=arp_display, filter="arp", store=0, count=0)
