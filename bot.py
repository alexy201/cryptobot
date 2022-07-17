import time
from datetime import datetime
import pandas as pd
import numpy as np
import ccxt
import cbpro
import constants

PUBLIC_API_KEY=constants.PUBLIC_API_KEY
SECRET_API_KEY=constants.SECRET_API_KEY
PASSPHRASE=constants.PASSPHRASE

auth_client = cbpro.AuthenticatedClient(PUBLIC_API_KEY, SECRET_API_KEY, PASSPHRASE)

sell_price = 25000
sell_amount = 0.3

buy_price = 20000
buy_amount = 0.2

while True:
    price = float(auth_client.get_product_ticker(product_id="BTC-USD")['price'])
    if price <= buy_price:
        print(f"Buying {buy_amount} units of BTC-USD because price of {price:,} fell below buying price limit of {buy_price}")
        auth_client.buy(size=buy_amount, order_type="market", product_id="BTC-USD")
    elif price >= sell_price:
        print(f"Selling {sell_amount} units of BTC-USD because price of {price:,} rose above selling price limit of {sell_price}")
        auth_client.sell(size=sell_amount, order_type="market", product_id="BTC-USD")
    else:
        print(f"Not doing anything. Price is {price:,}")
    time.sleep(10)
