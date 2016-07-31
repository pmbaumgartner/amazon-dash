from scapy.all import *
from pymongo import MongoClient
import datetime
import pytz

from time import sleep, time

client = MongoClient("mongodb://dog:dash@ds139425.mlab.com:39425/dog-dash")

db = client['dog-dash']

coll = db['records_collection']

last_mac = None

def arp_display(pkt):
    global last_mac
    if pkt[ARP].op == 1:
        MAC = pkt[ARP].hwsrc
        # print(MAC)

        # plum organics / ellis poop
        if MAC == '44:65:0d:a6:17:55' and MAC != last_mac:
            time_now = datetime.datetime.now(pytz.utc)
            coll.insert_one(
                {
                    'dog': 'Ellis',
                    'time': time_now,
                    'outcome' : 'poop'
                }
            )
            # print("Plum Organics detected")

        # chunky / miles poop
        if MAC == '44:65:0d:50:3b:dc' and MAC != last_mac:
            time_now = datetime.datetime.now(pytz.utc)
            coll.insert_one(
                {
                    'dog': 'Miles',
                    'time': time_now,
                    'outcome' : 'poop'
                }
            )
            # print("Chunky Soup detected")

        # litter genie / miles pee
        if MAC == '44:65:0d:b7:e1:35' and MAC != last_mac:
            time_now = datetime.datetime.now(pytz.utc)
            coll.insert_one(
                {
                    'dog': 'Miles',
                    'time': time_now,
                    'outcome' : 'pee'
                }
            )
            # print("Litter Genie detected")

        # glad / ellis pee
        if MAC == '44:65:0d:31:33:e5' and MAC != last_mac:
            time_now = datetime.datetime.now(pytz.utc)
            coll.insert_one(
                {
                    'dog': 'Ellis',
                    'time': time_now,
                    'outcome' : 'pee'
                }
            )
            # print("Glade detected")

        last_mac = MAC


sniff(prn=arp_display, filter="arp", store=0, count=0)
