"""This file will handle the communication with the Finnhub API, as well as package API data for 'tesla_utils'"""

import requests
import time
import datetime
import pandas as pd
import os

finn_key = 'c0b1ie748v6sc0gs1q40'

# go back to using this after work is done
# finn_key = os.getenv('FINN_KEY')


def current_price():
    """Returns the current price of Tesla"""

    r = requests.get(f'https://finnhub.io/api/v1/quote?symbol=TSLA&token={finn_key}')
    res = r.json()

    return res['c']


def gather_candle_data():
    """Gathers the data needed to make a candlestick chart"""

    # defining time range for api call (in UNIX)
    current_time_unix = int(time.time())
    six_months_ago_unix = int(time.time() - 15_780_000)

    df = pd.read_json(f'https://finnhub.io/api/v1/stock/candle?symbol=TSLA'
                      f'&resolution=D&from={six_months_ago_unix}&to={current_time_unix}&token={finn_key}')

    # convert unix time list in response dict to datetime list for x-axis in figure
    real_time = [datetime.datetime.fromtimestamp(int(x)).strftime('%Y-%m-%d') for x in df['t']]

    return df, real_time


def gather_eps_data():
    """Gathers the data required to make an EPS chart"""

    df = pd.read_json(f'https://finnhub.io/api/v1/stock/earnings?symbol=TSLA&token={finn_key}')

    return df


def gather_sma_data():
    """Returns data needed to create a moving average chart"""

    current_time_unix = int(time.time())
    # one month doesn't have enough data for 20 trading days sometimes.
    one_month_ago_unix = int(time.time() - 2_592_000)
    two_months_ago_unix = one_month_ago_unix - 2_592_000

    # We will use 6 months of data to create the SMA chart
    six_months_ago_unix = int(time.time() - 15_780_000)

    df = pd.read_json(f'https://finnhub.io/api/v1/stock/candle?symbol=TSLA'
                      f'&resolution=D&from={six_months_ago_unix}&to={current_time_unix}&token={finn_key}')

    # closing prices for time range specified
    closing_prices = [i for i in df['c']]
    moving_averages_20_day = []

    print(closing_prices)

    # Create counters to examine the last 20 closing prices
    i = 0
    j = 20

    # We start with 6 months of closing prices
    # The first point for our 20-day MA is the average of the first 20 closing prices

    # ma_val = sum(closing_prices[i:j]) / 20

    # print(first_value_ma)

    # First val was found with sum(1st val - 20th val) / 20
    # Our next value will be = sum(2nd val - 21st val) / 20
    # We examine 20 values at a time, and take the average. The average = our MA point to plot
    # Let's create a loop that finds the 20-day MA value for every point in 'closing_prices' (starting after 20 points)

    while j < len(closing_prices):
        # break this up
        ma_val = (sum(closing_prices[i:j]))
        ma_val = ma_val / 20
        moving_averages_20_day.append(ma_val)
        i += 1
        j += 1

    print(len(closing_prices))
    print(len(moving_averages_20_day))
    print(moving_averages_20_day)

    # at this point, the 20-day moving average list has 20-less vals than closing_prices.
    # we should start the chart plot with closing price 20 = first val in moving average

    return closing_prices, moving_averages_20_day


def gather_recommend_data():
    """Gathers information needed to create recommendation chart"""

    df = pd.read_json(f'https://finnhub.io/api/v1/stock/recommendation?symbol=TSLA&token={finn_key}')

    return df


def gather_news():
    """Gathers the latest news on Tesla"""

    # unix times:
    real_time_unix = int(time.time())
    one_month_ago_unix = int(time.time()) - 2_592_000

    # convert unix time to datetime:
    real_time = datetime.datetime.fromtimestamp(real_time_unix)
    one_month_ago = datetime.datetime.fromtimestamp(one_month_ago_unix)

    # format datetime for API query
    real_time = real_time.strftime('%Y-%m-%d')
    one_month_ago = one_month_ago.strftime('%Y-%m-%d')

    # query to receive last month of news on Tesla:
    df = pd.read_json(f'https://finnhub.io/api/v1/company-news?symbol=TSLA&from={one_month_ago}&to={real_time}&token={finn_key}')

    return df


gather_sma_data()