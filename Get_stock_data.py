import requests
import json


# Sample Function to get live stock data for a symbol (IBM)

stock_prices = {}
symbol = "IBM"
if price is not None:
    stock_prices[symbol] = price
    pstr = f"{price:4.2}"
    print(f"Current value of {symbol} share is : {f'${price:.6}'}")
else:
    print(f'Price is NONE !!!!')
