#!/usr/bin/python3.6

import requests
import json

def sats_to_usd(sats):

    sats = (sats / 100000000)

    while True:
        try:
            get_price = json.loads(
                requests.get('https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?limit=100&start=1').text
            )['data'][0]['quote']['USD']['price']

            return round(get_price * float(sats), 2)
        except KeyboardInterrupt: break
        except: pass
