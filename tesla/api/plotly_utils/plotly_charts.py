
import plotly
import plotly.graph_objs as go

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
