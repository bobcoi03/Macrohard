import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

import requests
import os
import json

financialmodelingprep_key = os.environ.get('financialmodelingprep_key')

r = requests.get(f"https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey={financialmodelingprep_key}")

gainers = json.loads(r.text)

ticker_symbol = gainers[0]['symbol']

stock = yf.Ticker(ticker_symbol)

price_data = stock.history(period="1mo", interval="2m")
print(price_data.size)

price_data['Open'].plot(label=ticker_symbol, figsize=(15,15))
plt.title(f'Stock price {ticker_symbol}')
plt.show()