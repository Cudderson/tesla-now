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
