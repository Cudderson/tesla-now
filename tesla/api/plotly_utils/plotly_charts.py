
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

    fig.update_layout(title='Tesla (TSLA) Candlestick Chart',
                    margin=go.layout.Margin(
                        l=25, #left margin
                        r=25, #right margin
                        b=20, #bottom margin
                        t=100, #top margin
                    ),
                    #   yaxis_title='Tesla Stock Price',
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
                                     marker=dict(size=[40, 40, 40, 40], color='#00FE35'),
                                     name='Actual'
                                    )])

    fig.add_trace(go.Scatter(x=custom_x_ticks, y=df['estimate'][::-1],
                             mode='markers',
                             marker=dict(size=[40, 40, 40, 40], color='#fe0d00'),
                             name='Estimate'
                            ))

    fig.update_layout(
        margin=go.layout.Margin(
            l=25, #left margin
            r=0, #right margin
            b=90, #bottom margin
            t=100, #top margin
        ),
        title={'text': 'Tesla EPS (Estimate vs Actual)',
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
        # yaxis_title='Earnings Per Share',
        # legend_title='EPS',
        # showlegend=False,
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

    fig.update_layout(
        title={
            'text': 'Tesla (TSLA) Simple Moving Averages',
            'x': .5,
            'y': .9,
        },
        # yaxis=dict(showticklabels=False),
        margin=go.layout.Margin(
            l=45, #left margin
            r=0, #right margin
            b=100, #bottom margin
            t=130, #top margin
        ),
        # yaxis_title='Closing Price vs SMA',
        legend=dict(x=.5, y=-0.25, xanchor='center', orientation='h', bgcolor='rgb(35, 35, 35)'),
        template='plotly_dark'
    )

    # chart = fig.to_html(full_html=False, default_height=700)

    # new method
    chart = plotly.offline.plot(fig, include_plotlyjs=False, output_type="div")

    return chart


def build_recommendation(df):
    # create lists of latest x months of data of recommendations. (x = num_recommendations) 
    num_recommendations = len(df)

    # (reversed with '[::-1]' to get oldest data first)
    strong_buy = [i for i in df['strongBuy'][:num_recommendations][::-1]]
    buy = [i for i in df['buy'][:num_recommendations]][::-1]
    hold = [i for i in df['hold'][:num_recommendations][::-1]]
    sell = [i for i in df['sell'][:num_recommendations][::-1]]
    strong_sell = [i for i in df['strongSell'][:num_recommendations][::-1]]
    period = [i for i in df['period'][:num_recommendations][::-1]]

    # Create stacked bar graph
    fig = go.Figure(data=[
        go.Bar(name='Strong Sell', x=period, y=strong_sell, marker_color='#8d423e'),
        go.Bar(name="Sell", x=period, y=sell, marker_color='#8d693e'),
        go.Bar(name="Hold", x=period, y=hold, marker_color='#473e8d'),
        go.Bar(name="Buy", x=period, y=buy, marker_color='#3e8d50'),
        go.Bar(name="Strong Buy", x=period, y=strong_buy, marker_color='#28a745'),
    ])

    fig.update_layout(
        title=dict(
            text="Recommendation Trends (TSLA)",
            x=.5,
            y=.9,
            xanchor='center',
        ),
        xaxis=dict(
            title='Date Reported',
            tickmode='array',
            tickvals=[i for i in period],
        ),
        yaxis_title='Number of Recommendations',
        barmode='stack',
        template='plotly_dark',
        )

    # chart = fig.to_html(full_html=False, default_height=800)

    # new method
    chart = plotly.offline.plot(fig, include_plotlyjs=False, output_type="div")

    return chart
