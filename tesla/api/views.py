# api views for rest framework

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import HelloWorldSerializer, PriceSerializer, HTMLChartPlotlySerializer

# maybe move these?
import os
finn_key = os.getenv('FINN_KEY')
import requests

# need these imports until ready to modularize
import time
import datetime
import pandas as pd
import plotly
import plotly.graph_objs as go

@api_view()
def hello_world(request):
    
    data = {"message": "Hello from Django Rest Framework!"}
    results = HelloWorldSerializer(data).data

    return Response(results)
    

# this works!
# hits the finnhub api and serializes the response for use by React 
@api_view()
def test_get_current_price(request):
    """Returns the current price of Tesla"""
    res = requests.get(f'https://finnhub.io/api/v1/quote?symbol=TSLA&token={finn_key}')
    data = res.json()
    print(data)
    serialized_data = PriceSerializer({'price': data}).data

    return Response(serialized_data)


# [x] successfully display candlestick chart in React
# in future, we will decouple code
@api_view()
def get_candlestick_chart(request):
    """
    returns a djangorestframework Response(serialized_data)
    """
    # doing everything here to make sure it works


    # defining time range for api call (in UNIX)
    current_time_unix = int(time.time())
    six_months_ago_unix = int(time.time() - 15_780_000)

    df = pd.read_json(f'https://finnhub.io/api/v1/stock/candle?symbol=TSLA'
                      f'&resolution=D&from={six_months_ago_unix}&to={current_time_unix}&token={finn_key}')

    # convert unix time list in response dict to datetime list for x-axis in figure
    real_time = [datetime.datetime.fromtimestamp(int(x)).strftime('%Y-%m-%d') for x in df['t']]

    # return df, real_time

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

    # at this point, we have an html representation of the chart.
    # we should serialize it and return a DRF Response
    serialized_data = HTMLChartPlotlySerializer({"chart": chart})
    # print(serialized_data.data) very long 

    # visiting 'localhost:8000/api/test-get-candlestick' correctly displays a dict: {chart: <div> object}
    return Response(serialized_data.data)
