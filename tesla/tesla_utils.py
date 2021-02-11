"""This file will contain utilities that view functions can use"""

# Finnhub 'quote' !!!
# create function that handles all api calls, once all graphs are complete.

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
    """Returns a candlestick chart in HTML format using a stock API and Pandas/Plotly"""

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
    chart = fig.to_html(full_html=False, default_height=500, default_width=700)

    # Returning our figure/graph to our 'home_page' view function on call
    return chart
    # fig.show()


def create_eps_chart():
    """Returns a EPS surprise chart in HTML format"""

    df = pd.read_json(f'https://finnhub.io/api/v1/stock/earnings?symbol=TSLA&token={config.finn_key}')

    # create custom ticks/labels for better UX/UI
    custom_x_ticks = [i for i in range(1, 5)]
    custom_x_labels = [i for i in df['period'][::-1]]

    # Iterate through dataframe backwards, to plot oldest data first
    fig = go.Figure(data=[go.Scatter(x=custom_x_ticks, y=df['actual'][::-1],
                                     mode='markers',
                                     marker=dict(size=[80, 80, 80, 80], color='#00FE35'),
                                     name='Actual')])

    fig.add_trace(go.Scatter(x=custom_x_ticks, y=df['estimate'][::-1],
                             mode='markers',
                             marker=dict(size=[80, 80, 80, 80], color='#fe0d00'),
                             name='Estimate'))

    fig.update_layout(
        title={'text': 'Tesla Earnings per Share (Estimate vs Actual)',
               'x': .5,
               'y': .9,
               'xanchor': 'center'},
        xaxis=dict(
            tickmode='array',
            tickvals=custom_x_ticks,
            ticktext=custom_x_labels,
            showgrid=False,
        ),
        xaxis_title='Date Reported',
        yaxis_title='Earnings Per Share',
        legend_title='Earnings Per Share',
        # plot_bgcolor='#727370' not a good color
    )

    chart = fig.to_html(full_html=False, default_height=500, default_width=700)
    return chart


def gather_sma_data():
    """Returns data needed to create a moving average chart"""

    current_time_unix = int(time.time())
    one_month_ago_unix = int(time.time() - 2_592_000)

    df = pd.read_json(f'https://finnhub.io/api/v1/stock/candle?symbol=TSLA'
                      f'&resolution=D&from={one_month_ago_unix}&to={current_time_unix}&token={config.finn_key}')

    # the number of entries we want
    n = 20

    # last 20 closing prices for time range specified
    last_20_prices = [i for i in df['c'][-20:]]
    moving_averages_20_day = []

    total = 0
    i = 1

    for price in last_20_prices:
        total += price
        sma_20 = total / i
        moving_averages_20_day.append(sma_20)
        i += 1

    return last_20_prices, moving_averages_20_day


def create_sma_chart():
    """Returns a simple moving average chart in HTML format"""

    last_20_prices, moving_averages_20_day = gather_sma_data()

    # 20 day moving average figure
    fig = go.Figure([go.Scatter(x=[i for i in range(len(moving_averages_20_day))], y=moving_averages_20_day)])

    # We also need to plot the closing prices of Tesla for the same time range.
    fig.add_trace(go.Scatter(x=[i for i in range(len(last_20_prices))], y=last_20_prices))

    # fig.show()
    # This chart works, can tweak it later! niiice

    chart = fig.to_html(full_html=False, default_height=600, default_width=800)

    return chart
