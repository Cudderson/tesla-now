
import plotly
import plotly.graph_objs as go

# df = pandas dataframe object

def build_candlestick(df, real_time):
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

    # from SO:
    # plotly.offline.plot(data, include_plotlyjs="cdn", output_type="div")
    # will give you a div with the necessary plotly js so that the div can just be embedded and you're done 

    # with 'include_plotly.js=False', we don't include any <scripts> to load Plotly within the HTML string
    # this is because plotly is linked in the <head> of our main index.html in React 
    chart = plotly.offline.plot(fig, include_plotlyjs=False, output_type="div")

    return chart


def build_eps(df):
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

    # this is the new method for converting charts
    chart = plotly.offline.plot(fig, include_plotlyjs=False, output_type="div")

    return chart


def build_sma(closing_prices, moving_averages_20_day, moving_averages_4_day, real_time):

    # build simple moving average chart

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

    # chart = fig.to_html(full_html=False, default_height=700)

    # new method
    chart = plotly.offline.plot(fig, include_plotlyjs=False, output_type="div")

    return chart


def build_recommendation(df):
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

    # chart = fig.to_html(full_html=False, default_height=800)

    # new method
    chart = plotly.offline.plot(fig, include_plotlyjs=False, output_type="div")

    return chart
