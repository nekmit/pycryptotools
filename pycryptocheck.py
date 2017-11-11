'''
PyCryptoCheck - Using CoinMarketCap API to fetch prices (used to be MoneroCheck)
Made by nekmit for nekmit (cuz CAD)
'''

import sys
import os
import json
import requests
import socket
import argparse

def MainActivity():
	# ArgParsing
	p = argparse.ArgumentParser()
	p.add_argument("coin", help="Coin to view")
	args = p.parse_args()
	api = "https://api.coinmarketcap.com/v1/ticker/{}/?convert=CAD".format(args.coin)
	req = requests.get(api, headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"})
	
	if(req.status_code == 200):
		txt = json.loads(req.text)
		print("Data from {}".format(txt[0]["symbol"]))
		print("Price: ${} CAD".format(txt[0]["price_cad"]))
		print("{} Left: {} {}".format(txt[0]["symbol"], txt[0]["available_supply"], txt[0]["symbol"]))
		print("Most Recent Percent Change: {}%".format(txt[0]["percent_change_1h"]))
if __name__ == '__main__':
	MainActivity()