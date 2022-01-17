# Communicates with the Finnhub.io API and returns Tesla data for charts

import pandas as pd
import time
import datetime
import os
import requests

# could pass the key as a param?
finn_key = os.getenv('FINN_KEY')

def get_current_price_data():
    """Returns the current price of Tesla"""

    r = requests.get(f'https://finnhub.io/api/v1/quote?symbol=TSLA&token={finn_key}')
    res = r.json()

    return res['c']

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

    # print(closing_prices)

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


def get_recommendation_data():
    df = pd.read_json(f'https://finnhub.io/api/v1/stock/recommendation?symbol=TSLA&token={finn_key}')
    return df


def get_news_data():
    """Gathers the latest news on Tesla"""

    # unix times:
    real_time_unix = int(time.time())
    one_month_ago_unix = int(time.time()) - 2_592_000
    # two_weeks_ago_unix = int(time.time()) - 1_209_600
    # one_week_ago_unix = int(time.time()) - 604800

    # convert unix time to datetime:
    real_time = datetime.datetime.fromtimestamp(real_time_unix)
    one_month_ago = datetime.datetime.fromtimestamp(one_month_ago_unix)
    # two_weeks_ago = datetime.datetime.fromtimestamp(two_weeks_ago_unix)
    # one_week_ago = datetime.datetime.fromtimestamp(one_week_ago_unix)

    # format datetime for API query
    real_time = real_time.strftime('%Y-%m-%d')
    one_month_ago = one_month_ago.strftime('%Y-%m-%d')
    # two_weeks_ago = two_weeks_ago.strftime('%Y-%m-%d')
    # one_week_ago = one_week_ago.strftime('%Y-%m-%d')

    # query to receive news on Tesla:
    df = pd.read_json(f'https://finnhub.io/api/v1/company-news?symbol=TSLA&from={one_month_ago}&to={real_time}&token={finn_key}')

    return df


def create_news_package(df):
    """Packages news data into a dictionary structure for easy handling"""

    # df = tesla_api.gather_news()

    headlines = []
    times_posted = []
    urls = []
    summaries = []
    images = []
    sources = []
    i = 0

    # grabbing news data we want based on headlines containing 'tesla' or 'elon'
    # sometimes we receive duplicate articles, so we filter the extras out
    for news in df['headline'][:25]:
        if news not in headlines and news:
            if 'tesla' in news.lower() or 'elon' in news.lower():
                headlines.append(news)
                times_posted.append(df['datetime'][i])
                urls.append(df['url'][i])
                summaries.append(df['summary'][i])
                images.append(df['image'][i])
                sources.append(df['source'][i].title())
            i += 1

    # create nested lists for news data received
    # full_news_data = [
    #     times_posted,
    #     headlines,
    #     summaries,
    #     urls,
    #     images,
    #     sources,
    # ]

    # a dictionary would be so much better here
    full_news_data = {
        'times_posted': times_posted,
        'headlines': headlines,
        'summaries': summaries,
        'urls': urls,
        'images': images,
        'sources': sources,
    }

    # print(full_news_data['headlines'][0]) <- example
    return full_news_data
