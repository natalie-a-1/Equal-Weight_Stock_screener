# Project aims to create an alternate version of S&P 500
# Instead of capitalization-weight between companies
# Each company has an equal-weight
# Potential to schedule this script to run automatically
import pandas as pd
import requests
import math
import random
from secretsFile import ALPHA_API_KEY

api_url = f'https://www.alphavantage.co/query'
columns = ['Ticker', 'Stock Price', 'Market Capitalization', 'Number of Shares to Buy']
stocks = pd.read_csv('starter-files/sp_500_stocks.csv')
data_list = []


def GenerateMarketCap():
    min_value = 100000000.00
    max_value = 50000000000.00
    return random.uniform(min_value, max_value)


# Ideally use batch API calls
# However, alpha vantage does NOT support this functionality
def SingleAPICalls():
    for stock in stocks['Ticker']:
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': stock,
            'apikey': ALPHA_API_KEY
        }
        response = requests.get(api_url, params=params).json()

        if 'Global Quote' in response:
            try:
                # Extract the required data from the API response
                data = response['Global Quote']
                stock_price = float(data['05. price'])

                # generate random num for market cap
                # because api does NOT provide &
                # I am too broke to pay for a plan :)
                market_cap = GenerateMarketCap()

                # Append the data to the list
                temp_list = [stock, stock_price, market_cap, 'N/A']
                data_list.append(temp_list)
            except KeyError as e:
                print(f"Error accessing data for {stock}: {e}")
        else:
            print(f"Error in accessing data for {stock} from Alpha Vantage")
    df = pd.DataFrame(data_list, columns=columns)
    return df


# For performing batch api calls
def Chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


portfolio_size = input("Enter the value of your portfolio: ")
try:
    val = float(portfolio_size)
except ValueError:
    print("Please enter a number. \n")
    portfolio_size = input("Enter the value of your portfolio: ")
    val = float(portfolio_size)
final_df = SingleAPICalls()
position_size = val/len(final_df.index)
for i in range(0, len(final_df.index)):
    final_df.loc[i, 'Number of Shares to Buy' ] = math.floor(position_size/final_df.loc[i, 'Stock Price'])

writer = pd.ExcelWriter('RecommendedTrades.xlsx', engine='xlsxwriter')
final_df.to_excel(writer, 'Recommended Trades', index=False)

background_color = '#0a0a23'
font_color = '#ffffff'

string_format = writer.book.add_format(
    {
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1
    }
)

dollar_format = writer.book.add_format(
    {
        'num_format': '$0.00',
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1
    }
)

integer_format = writer.book.add_format(
    {
        'num_format': '0',
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1
    }
)

writer.sheets['Recommended Trades'].write('A1', 'Ticker', string_format)
writer.close()

column_formats = {
    'A': ['Ticker', string_format],
    'B': ['Stock Price', dollar_format],
    'C': ['Market Capitalization', dollar_format],
    'D': ['Number of Shares to Buy', integer_format]
}

for column in column_formats.keys():
    writer.sheets['Recommended Trades'].set_column(f'{column}:{column}', 18, column_formats[column][1])
    writer.sheets['Recommended Trades'].write(f'{column}1', 18, column_formats[column][0], column_formats[column][1])
writer.close()