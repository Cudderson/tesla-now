# Communicates with the Finnhub.io API and returns Tesla data for charts

import pandas as pd
import time
import datetime
import os

# could pass the key as a param?
finn_key = os.getenv('FINN_KEY')

def get_candlestick_data():
    # defining time range for api call (in UNIX)
    current_time_unix = int(time.time())
    six_months_ago_unix = int(time.time() - 15_780_000)

    df = pd.read_json(f'https://finnhub.io/api/v1/stock/candle?symbol=TSLA'
                      f'&resolution=D&from={six_months_ago_unix}&to={current_time_unix}&token={finn_key}')

    # convert unix time list in response dict to datetime list for x-axis in figure
    real_time = [datetime.datetime.fromtimestamp(int(x)).strftime('%Y-%m-%d') for x in df['t']]

    return df, real_time

def get_eps_data():
  
    df = pd.read_json(f'https://finnhub.io/api/v1/stock/earnings?symbol=TSLA&token={finn_key}')
    return df


# make sure calcs are correct here, maybe decouple
def get_sma_data():
    current_time_unix = int(time.time())

    # We will use 6 months of data to create the SMA chart
    six_months_ago_unix = int(time.time() - 15_780_000)

    df = pd.read_json(f'https://finnhub.io/api/v1/stock/candle?symbol=TSLA'
                      f'&resolution=D&from={six_months_ago_unix}&to={current_time_unix}&token={finn_key}')

    # Formatted dates for x-axis
    real_time = [datetime.datetime.fromtimestamp(int(x)).strftime('%Y-%m-%d') for x in df['t']]

    # closing prices for time range specified
    closing_prices = [i for i in df['c']]
    moving_averages_20_day = []
    moving_averages_4_day = []

    print(closing_prices)

    # counters to examine a range of 20 closing prices
    i = 0
    j = 20

    # counters to examine a range of 4 closing prices
    n = 16
    m = 20

    # Generate list representing values for 20-day moving average
    while j < len(closing_prices):

        average_20_day = (sum(closing_prices[i:j])) / 20
        moving_averages_20_day.append(average_20_day)

        i += 1
        j += 1

    while m < len(closing_prices):

        average_4_day = (sum(closing_prices[n:m])) / 4
        moving_averages_4_day.append(average_4_day)

        n += 1
        m += 1

    return closing_prices, moving_averages_20_day, moving_averages_4_day, real_time
