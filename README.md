# Equal-Weight S&P 500 Project

## Project Overview

The aim of this project is to create an alternate version of the S&P 500 index where each company has an equal-weight instead of the usual capitalization-weighted structure. The script fetches stock price data and generates random market capitalization values for each company in the S&P 500 index using the Alpha Vantage API. The generated data is then used to calculate the number of shares to buy for each company based on the specified portfolio value.

## Getting Started

To run this project, you need to have Python installed on your machine. Additionally, you should have the required packages installed, which include `pandas` and `requests`. You also need an API key from Alpha Vantage, which should be placed in a file named `secretsFile.py` as the variable `ALPHA_API_KEY`.

## Project Workflow

1. The script reads the list of S&P 500 companies and tickers from the CSV file `sp_500_stocks.csv`.

2. The function `GenerateMarketCap()` is used to generate random market capitalization values for each company since Alpha Vantage does not provide this information. The range of market capitalization is set between 100 million to 50 billion.

3. The function `SingleAPICalls()` iterates through each company's ticker, performs individual API calls to Alpha Vantage to get stock price data, and appends the required data (Ticker, Stock Price, Market Capitalization, Number of Shares to Buy) to a list.

4. The user is prompted to enter the value of their portfolio. The script calculates the position size for each company based on the equal-weighting strategy.

5. The final data is stored in a Pandas DataFrame, and the number of shares to buy for each company is calculated based on the position size.

6. The data is written to an Excel file named `RecommendedTrades.xlsx` using `pd.ExcelWriter` and `df.to_excel()`.

7. The Excel file's appearance is customized with background colors and formats using the `xlsxwriter` library.

## Running the Script

1. Install the required Python packages:

```bash
pip install pandas requests openpyxl xlsxwriter
```

2. Create a file named `secretsFile.py` and store your Alpha Vantage API key as follows:

```python
ALPHA_API_KEY = "your_api_key_here"
```

3. Make sure the `sp_500_stocks.csv` file is in the same directory as the script.

4. Run the script, and it will prompt you to enter the value of your portfolio.

5. The script will generate the recommended trades based on the equal-weight strategy and save them in `RecommendedTrades.xlsx`.

## Customizing the Output

You can modify the appearance of the Excel output by changing the `background_color` and `font_color` variables in the script. Additionally, you can adjust the format of columns (Ticker, Stock Price, Market Capitalization, Number of Shares to Buy) in the Excel file by modifying the respective `string_format`, `dollar_format`, and `integer_format` variables.

## Schedule the Script

To schedule the script to run automatically, you can use task scheduler or cron jobs on your operating system. Set up the scheduling interval according to your preference (e.g., daily, weekly, etc.) to keep the data up to date.

Please note that the Alpha Vantage API might have rate limits for free users, so it's essential to check their terms of use and rate limits before scheduling frequent updates.

## Disclaimer

This project is for educational and informational purposes only and does not constitute financial advice. Trading and investing in the stock market involve risks, and you should consult with a qualified financial advisor before making any investment decisions.

## Feedback and Contributions

Feedback and contributions to improve this project are welcome! If you find any issues or have suggestions for enhancements, feel free to open an issue or submit a pull request on the project repository.

---

**Disclaimer:** The information provided in this document is based on the code and project description provided. The author assumes no responsibility for the accuracy, completeness, or use of the information contained herein. The user of this code and information should carefully review the code, adapt it to their needs, and use it at their own risk.
