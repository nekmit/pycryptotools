'''
MCAN - Make Crypto API Nicer
Python3 script that uses Flask to make an API that uses an API to make it look cleaner and display what you need

A piece of the PyCryptoTools project (used to be PyCryptoCheck)

Made by Nekmit (nekmit@riseup.net)
'''

# import some stuff
import os
import sys
import requests
import json
import socket
import flask
from flask import *

app = Flask('mcan')

@app.route('/<string:coin>')
def GetCryptoData(coin):
	api = "http://api.coinmarketcap.com/v1/ticker/{}/?convert=CAD".format(coin)
	req = requests.get(api, headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"})
	if req.status_code == 200:
		txt = json.loads(req.text)
		return jsonify(
		coin_used=txt[0]["symbol"],
		price_cad=txt[0]["price_cad"],
		price_usd=txt[0]["price_usd"],
		coins_left=txt[0]["available_supply"],
		latest_change="{}%".format(txt[0]["percent_change_1h"])
		)
if __name__ == '__main__':
	app.run(host='localhost', port=420)
