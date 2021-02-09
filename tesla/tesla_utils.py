"""This file will contain utilities that view functions can use"""

# Finnhub 'quote' !!!

import requests
import config
import time
import datetime
import pandas as pd
import plotly.graph_objs as go


def current_price():
    """Returns the current price of Tesla"""

    r = requests.get(f'https://finnhub.io/api/v1/quote?symbol=TSLA&token={config.finn_key}')
    res = r.json()

    return res['c']


def create_candle_chart():
    """Returns a candlestick chart using a stock API and Pandas/Plotly"""

    # defining time range for api call (in UNIX)
    current_time_unix = int(time.time())
    six_months_ago_unix = int(time.time() - 15_780_000)
    # one_month_ago_unix = int(time.time() - 2_592_000)
    # three_months_ago_unix = int(time.time() - 7_776_000)

    df = pd.read_json(f'https://finnhub.io/api/v1/stock/candle?symbol=TSLA'
                      f'&resolution=D&from={six_months_ago_unix}&to={current_time_unix}&token={config.finn_key}')

    # convert unix time list in response dict to datetime list for x-axis in figure
    real_time = [datetime.datetime.fromtimestamp(int(x)).strftime('%Y-%m-%d') for x in df['t']]

    # create figure using 'OHLC' Tesla data
    fig = go.Figure(data=[go.Candlestick(x=real_time, open=df['o'], high=df['h'], low=df['l'], close=df['c'])])

    # Converting figure into HTML format
    graph = fig.to_html(full_html=False, default_height=500, default_width=700)

    # Returning our figure/graph to our 'home_page' view function on call
    return graph
    # fig.show()
