import time
from datetime import datetime
import pandas as pd
import numpy as np
import ccxt
import constants

PUBLIC_API_KEY=constants.PUBLIC_API_KEY
SECRET_API_KEY=constants.SECRET_API_KEY
PASSPHRASE=constants.PASSPHRASE

exchange_id = 'coinbasepro'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': PUBLIC_API_KEY,
    'secret': SECRET_API_KEY,
    'password': PASSPHRASE
})
#exchange.set_sandbox_mode(True) 
markets = exchange.load_markets()

buy_price = 21430
buy_amount = 1

sell_price = 21450
sell_amount = 1

balance = 50000
holding = 0
fee = 99.4

while True:
    price = (float(exchange.fetchTicker("BTC/USD")['info']['bid']) + float(exchange.fetchTicker("BTC/USD")['info']['ask']))/2.0
    if price <= buy_price:
        print(f"Buying {buy_amount} units of BTC-USD because price of {price:,} fell below buying price limit of {buy_price}")
        balance -= float(exchange.fetchTicker("BTC/USD")['info']['bid'])
        balance *= fee
        holding += 1
        #auth_client.buy(size=buy_amount, order_type="market", product_id="LINK-USD")
    elif price >= sell_price and holding > 0:
        print(f"Selling {sell_amount} units of BTC-USD because price of {price:,} rose above selling price limit of {sell_price}")
        balance += float(exchange.fetchTicker("BTC/USD")['info']['ask'])
        balance *= fee
        holding -= 1
        #auth_client.sell(size=sell_amount, order_type="market", product_id="LINK-USD")
    else:
        print(f"Not doing anything. Price is {price:,}")
    time.sleep(10)


#btc_usd_ohlcv = exchange.fetch_ohlcv('BTC/USD','1d',limit=100)
#for row in btc_usd_ohlcv:
#    print(row)