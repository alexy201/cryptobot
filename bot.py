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

public_client = cbpro.PublicClient()
result = public_client.get_product_24hr_stats('BTC-USD')

auth_client = cbpro.AuthenticatedClient(PUBLIC_API_KEY, SECRET_API_KEY, PASSPHRASE)

print(auth_client.buy(price="0", size="2.1", order_type="limit", product_id="ETH-USD")) #limit
auth_client.place_limit_order(product_id="BTC-USD", side="buy", price="10.0",size="2")
print(auth_client.buy(size="10", order_type="market", product_id="ETH-USD")) #market

print(auth_client.sell(price="20000000.00", size="10", order_type="limit", product_id="BTC-USD"))
print(auth_client.sell(size="10", order_type="market", product_id="BTC-USD")) #market
print(auth_client.cancel_all(product_id="BTC_USD"))

auth_client.get_orders()


sell_price = 30000
sell_amount = 0.3

buy_price = 25000
buy_amount = 0.2

while True:
    price = float(auth_client.get_product_ticker(product_id="BTC-USD")['price'])
    if price <= buy_price:
        print("BUYING BTC")
        auth_client.buy(size=buy_amount, order_type="market", product_id="BTC-USD")
    elif price >= sell_price:
        print("SELLING BTC")
