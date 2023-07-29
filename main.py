# Project aims to create an alternate version of S&P 500
# Instead of capitalization-weight between companies
# Each company has an equal-weight
import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from secretsFile import IEX_CLOUD_API_TOKEN

# import list of stocks
stocks = pd.read_csv('starter-files/sp_500_stocks.csv')
symbol = 'AAPL'
api_url = f'https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
price = data['latestPrice']
market_cap = data['marketCap']
