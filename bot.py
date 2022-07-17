import time
from datetime import datetime
import pandas as pd
import numpy as np
import ccxt
import constants

#PUBLIC_API_KEY=constants.FAKE_PUBLIC_API_KEY
#SECRET_API_KEY=constants.FAKE_SECRET_API_KEY
#PASSPHRASE=constants.FAKE_PASSPHRASE

PUBLIC_API_KEY=constants.PUBLIC_API_KEY
SECRET_API_KEY=constants.SECRET_API_KEY
PASSPHRASE=constants.PASSPHRASE

#auth_client = cbpro.AuthenticatedClient(PUBLIC_API_KEY, SECRET_API_KEY, PASSPHRASE, api_url="https://api-public.sandbox.pro.coinbase.com")
auth_client = cbpro.AuthenticatedClient(PUBLIC_API_KEY, SECRET_API_KEY, PASSPHRASE)

sell_price = 25000
sell_amount = 1

buy_price = 0
buy_amount = 1


#coins = auth_client.get_products();
#N = 0
#for row in coins:
#    if row['quote_currency'] != 'USD' or row['trading_disabled'] == True:
#        continue
#    N = N + 1
#    try:
#        price = float(auth_client.get_product_ticker(product_id=row['id'])['price'])
#        print(price)
#    except:
#        print("Error fetching coin price")
#print(N)




while True:
    price = float(auth_client.get_product_ticker(product_id="LINK-USD")['price'])
    if price <= buy_price:
        print(f"Buying {buy_amount} units of LINK-USD because price of {price:,} fell below buying price limit of {buy_price}")
        auth_client.buy(size=buy_amount, order_type="market", product_id="LINK-USD")
    elif price >= sell_price:
        print(f"Selling {sell_amount} units of LINK-USD because price of {price:,} rose above selling price limit of {sell_price}")
        auth_client.sell(size=sell_amount, order_type="market", product_id="LINK-USD")
    else:
        print(f"Not doing anything. Price is {price:,}")
    time.sleep(10)
