"""This file will contain utilities that build figures for view functions to use"""

import plotly.graph_objs as go
from . import tesla_api


def create_candle_chart():
    """Returns a candlestick chart in HTML format using a stock API and Pandas/Plotly"""

    df, real_time = tesla_api.gather_candle_data()

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
    # chart = fig.to_html(full_html=False, default_height=800, default_width=1200)
    chart = fig.to_html(full_html=False, default_height=600)

    # Returning our figure/graph to our 'home_page' view function on call
    return chart


def create_eps_chart():
    """Returns a EPS surprise chart in HTML format"""

    df = tesla_api.gather_eps_data()

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

    chart = fig.to_html(full_html=False, default_height=600)
    return chart


def create_sma_chart():
    """Returns a simple moving average chart in HTML format"""

    closing_prices, moving_averages_20_day, moving_averages_4_day, real_time = tesla_api.gather_sma_data()

    fig = go.Figure()

    # 20 day moving average figure
    fig.add_trace(go.Scatter(
        name='20-day SMA', mode='lines',
        x=real_time[20:],
        y=moving_averages_20_day,
        line=dict(color='#fe0d00')))

    # 4 day moving average figure
    fig.add_trace(go.Scatter(
        name='4-day SMA', mode='lines',
        x=real_time[20:],
        y=moving_averages_4_day,
        line=dict(color='#00cbfe')
    ))

    # Closing prices figure
    fig.add_trace(go.Scatter(
        name='Closing Price', mode='lines',
        x=real_time[20:],
        y=closing_prices[20::],
        line=dict(color='#66fe00')))

    # highlighting latest closing price
    fig.add_trace(go.Scatter(
        name='Latest Closing Price', mode='markers', x=[real_time[-1]], y=closing_prices[-1:],
        marker=dict(
            size=15,
            color='#66fe00',
            opacity=.8
        ), showlegend=False
    ))

    # highlighting latest 20 day moving average level
    fig.add_trace(go.Scatter(
        name='Current SMA20 Level', mode='markers', x=[real_time[-1]], y=moving_averages_20_day[-1:],
        marker=dict(
            size=15,
            color='#fe0d00',
            opacity=.8
        ), showlegend=False
    ))

    # highlighting latest 4 day moving average level
    fig.add_trace(go.Scatter(
        name='Current SMA4 Level', mode='markers', x=[real_time[-1]], y=moving_averages_4_day[-1:],
        marker=dict(
            size=15,
            color='#00cbfe',
            opacity=.8
        ), showlegend=False
    ))

    # Format figure (UI)
    fig.update_yaxes(tickprefix='$')

    fig.update_layout(title_text='Simple Moving Averages: TSLA',
                      yaxis_title='Closing Price vs SMA',
                      template='plotly_dark')

    chart = fig.to_html(full_html=False, default_height=700)

    return chart


def create_recommend_chart():
    """Returns a recommendation trend chart in HTML format"""

    df = tesla_api.gather_recommend_data()

    # create lists of latest 6 months of data of recommendations. (reversed with '[::-1]' to get oldest data first)
    strong_buy = [i for i in df['strongBuy'][:6][::-1]]
    buy = [i for i in df['buy'][:6]][::-1]
    hold = [i for i in df['hold'][:6][::-1]]
    sell = [i for i in df['sell'][:6][::-1]]
    strong_sell = [i for i in df['strongSell'][:6][::-1]]
    period = [i for i in df['period'][:6][::-1]]

    # Create stacked bar graph
    fig = go.Figure(data=[
        go.Bar(name='Strong Sell', x=period, y=strong_sell, marker_color='#8d423e'),
        go.Bar(name="Sell", x=period, y=sell, marker_color='#8d693e'),
        go.Bar(name="Hold", x=period, y=hold, marker_color='#473e8d'),
        go.Bar(name="Buy", x=period, y=buy, marker_color='#3e8d50'),
        go.Bar(name="Strong Buy", x=period, y=strong_buy, marker_color='#28a745'),
    ])

    fig.update_layout(
        title_text='Tesla',
        yaxis_title='Number of Recommendations',
        barmode='stack',
        template='plotly_dark',
        )

    chart = fig.to_html(full_html=False, default_height=800)
    return chart


def create_news_package():
    """Packages news data into a dictionary structure for easy handling"""

    df = tesla_api.gather_news()

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
    full_news_data = [
        times_posted,
        headlines,
        summaries,
        urls,
        images,
        sources,
    ]

    # print(full_news_data['headlines'][0]) <- example
    return full_news_data


def about_page_data():
    """Holds information for the 'about' page to be passed to a view"""

    what_is_this = 'What is Tesla Now?'

    what_it_is = 'Tesla Now is a personal project that is designed ' \
                 'as an investment tool and central location for all things Tesla.'

    project_details = 'Built with Django, this project gathers Tesla-related information in real-time ' \
                      'with the help of the Finnhub.io API. Tesla Now ' \
                      'uses fresh-data to build interactive-charts and supply ' \
                      'the newest articles to the user, as soon as they are published.'

    about_the_creator = "My name is Cody and I'm an aspiring software developer. I created this project " \
                        "due not only to my love for Tesla, but as a showcase for my programming abilities as well. " \
                        "If you enjoyed the project, please consider giving it a 'star' on Github. Feel free to " \
                        "contact me for anything related to this project, hiring, or programming! " \
                        "(links below)"

    disclaimer = 'Tesla Now is a non-monetized project with no affiliation to Tesla Inc.'

    finnhub_url = 'https://finnhub.io/'

    my_github_profile = 'http://github.com/cudderson/tesla-now'

    tesla_url = 'https://www.tesla.com/'

    about_package = [
        what_is_this,
        what_it_is,
        project_details,
        about_the_creator,
        disclaimer,
        finnhub_url,
        my_github_profile,
        tesla_url,
    ]

    return about_package
