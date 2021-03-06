#!/usr/bin/python3

import sys
import time
import requests
import json

# Initialize
last_update = 0
got_status = ""

# coinmarketcap.com has an API query interval of 10s
interval_secs = 15

def get_stats():
        ccStats = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=10')
        if isinstance(ccStats.json(), list):
            last_update = int(time.time())
            return ccStats.json()


# Pull initial values upon start
stats = get_stats()

# Infinitely loop thru parsing the stats into a top-10 list of rank, coin, and USD value
while True:
    if int(last_update) + interval_secs < int(time.time()):
        stats = get_stats()
    for i in stats:
        price = format(float(i['price_usd']), '.2f')
        print(i['rank'].zfill(2) + " " + i['id'] + " " + "$" + price)
    print()
    time.sleep(interval_secs)
