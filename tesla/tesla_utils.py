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
    fig = go.Figure(data=[go.Candlestick(
        x=real_time,
        open=df['o'],
        high=df['h'],
        low=df['l'],
        close=df['c'],
        increasing_line_color='#00FE35',
        decreasing_line_color='#fe0d00',
    )])

    fig.update_layout(title='Tesla Now Candlestick (6 Months)',
                      yaxis_title='Tesla Stock Price',
                      title_x=0.5,
                      template='plotly_dark'
                      )

    # Converting figure into HTML format
    chart = fig.to_html(full_html=False, default_height=800, default_width=1200)

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
        template='plotly_dark'
    )

    chart = fig.to_html(full_html=False, default_height=600, default_width=1200)
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

    fig = go.Figure()

    # 20 day moving average figure
    fig.add_trace(go.Scatter(
        name='20-day SMA',
        x=[i+1 for i in range(len(moving_averages_20_day))],
        y=moving_averages_20_day,
        line=dict(color='#fe0d00')))

    # Closing prices figure
    fig.add_trace(go.Scatter(
        name='Closing Price',
        x=[i+1 for i in range(len(last_20_prices))],
        y=last_20_prices,
        line=dict(color='#00FE35')))

    # highlighting latest closing price
    fig.add_trace(go.Scatter(
        name='Latest Closing Price', mode='markers', x=[20], y=last_20_prices[-1:],
        marker=dict(
            size=15,
            color='#00FE35',
            opacity=.8
        ), showlegend=False
    ))

    # highlighting latest moving average level
    fig.add_trace(go.Scatter(
        name='Current SMA Level', mode='markers', x=[20], y=moving_averages_20_day[-1:],
        marker=dict(
            size=15,
            color='#fe0d00',
            opacity=.8
        ), showlegend=False
    ))

    # Format figure (UI)
    fig.update_xaxes(type='category', range=[0, 20])
    fig.update_yaxes(tickprefix='$')

    fig.update_layout(title_text='20-day Simple Moving Average: TSLA',
                      xaxis_title='20-day Period (Trading Days)',
                      yaxis_title='Closing Price vs SMA',
                      template='plotly_dark')

    chart = fig.to_html(full_html=False, default_height=600, default_width=1200)

    return chart


def gather_recommend_data(): #  save just incase
    """Gathers information needed to create recommendation chart"""

    df = pd.read_json(f'https://finnhub.io/api/v1/stock/recommendation?symbol=TSLA&token={config.finn_key}')


def create_recommend_chart():
    """Returns a recommendation trend chart in HTML format"""

    df = pd.read_json(f'https://finnhub.io/api/v1/stock/recommendation?symbol=TSLA&token={config.finn_key}')

    # create lists of latest 6 months of data of recommendations. (reversed with '[::-1]' to get oldest data first)
    strong_buy = [i for i in df['strongBuy'][:6][::-1]]
    buy = [i for i in df['buy'][:6]][::-1]
    hold = [i for i in df['hold'][:6][::-1]]
    sell = [i for i in df['sell'][:6][::-1]]
    strong_sell = [i for i in df['strongSell'][:6][::-1]]
    period = [i for i in df['period'][:6][::-1]]

    # Create stacked bar graph, can optimize later
    fig = go.Figure(data=[
        go.Bar(name='Strong Sell', x=period, y=strong_sell, marker_color='#8d423e'),
        go.Bar(name="Sell", x=period, y=sell, marker_color='#8d693e'),
        go.Bar(name="Hold", x=period, y=hold, marker_color='#473e8d'),
        go.Bar(name="Buy", x=period, y=buy, marker_color='#3e8d50'),
        go.Bar(name="Strong Buy", x=period, y=strong_buy, marker_color='#28a745'),
    ])

    fig.update_layout(
        barmode='stack',
        template='plotly_dark',
        )

    chart = fig.to_html(full_html=False, default_height=800, default_width=1200)
    return chart


def gather_news():
    """Gathers the latest news on Tesla"""

    #  example: 'https://finnhub.io/api/v1/company-news?symbol=AAPL&from=2020-04-30&to=2020-05-01&token=c0b1ie748v6sc0gs1q40'

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
    df = pd.read_json(f'https://finnhub.io/api/v1/company-news?symbol=TSLA&from={one_month_ago}&to={real_time}&token={config.finn_key}')

    return df


def create_news_package():
    """Packages news data into a dictionary structure for easy handling"""

    df = gather_news()

    headlines = []
    times_posted = []
    urls = []
    summaries = []
    images = []
    i = 0

    # grabbing news data we want based on headlines containing 'tesla' or 'elon'
    for news in df['headline'][:10]:
        if 'tesla' in news.lower() or 'elon' in news.lower():
            headlines.append(news)
            times_posted.append(df['datetime'][i])
            urls.append(df['url'][i])
            summaries.append(df['summary'][i])
            images.append(df['image'][i])
        i += 1

    # create dictionary for news data received
    full_news_data = {
        'headlines': headlines,
        'times_posted': times_posted,
        'urls': urls,
        'summaries': summaries,
        'images': images,
    }

    # print(full_news_data['headlines'][0]) <- example
    return full_news_data
