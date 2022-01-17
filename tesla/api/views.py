# api views for rest framework

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import HTMLChartPlotlySerializer, NewsDataSerializer, PriceSerializer

from .pandas_utils import finnhub_data
from .plotly_utils import plotly_charts

# maybe move these?
# import os
# finn_key = os.getenv('FINN_KEY')
import requests

# need these imports until ready to modularize
# import time
# import datetime
# import pandas as pd
# import plotly
# import plotly.graph_objs as go

# saving these as examples
#
# @api_view()
# def hello_world(request):
    
#     data = {"message": "Hello from Django Rest Framework!"}
#     results = HelloWorldSerializer(data).data

#     return Response(results)
    

# @api_view()
# def test_get_current_price(request):
#     """Returns the current price of Tesla"""
#     res = requests.get(f'https://finnhub.io/api/v1/quote?symbol=TSLA&token={finn_key}')
#     data = res.json()
#     print(data)
#     serialized_data = PriceSerializer({'price': data}).data

#     return Response(serialized_data)

@api_view()
def get_current_price(request):
    """
    returns a djangorestframework Response(serialized_data)
    """

    raw_current_price_data = finnhub_data.get_current_price_data()

    serialized_data = PriceSerializer({"current_price": raw_current_price_data})

    return Response(serialized_data.data)

# in future, we will decouple code
@api_view()
def get_candlestick_chart(request):
    """
    returns a djangorestframework Response(serialized_data)
    """
    
    candlestick_data_json, real_time = finnhub_data.get_candlestick_data()

    # candlestick_chart is an HTML string representation of a plotly chart
    candlestick_chart = plotly_charts.build_candlestick(candlestick_data_json, real_time)
    
    # serialize and return a DRF Response
    serialized_data = HTMLChartPlotlySerializer({"chart": candlestick_chart})
    # print(serialized_data.data) very long 

    # visiting 'localhost:8000/api/test-get-candlestick' correctly displays a dict: {chart: <div> object}
    return Response(serialized_data.data)


# Next, let's get the EPS chart
@api_view()
def get_EPS_chart(request):
    """
    Returns a DRF Response with a serialized html string representing a Plotly chart
    """

    eps_data_json = finnhub_data.get_eps_data()

    # eps_chart is an HTML string representation of a plotly chart
    eps_chart = plotly_charts.build_eps(eps_data_json)
    
    serialized_data = HTMLChartPlotlySerializer({"chart": eps_chart})

    return Response(serialized_data.data)

@api_view()
def get_SMA_chart(request):
    """
    Returns a DRF Response with a serialized html string representing a Plotly chart
    """

    # consider decoupling
    closing_prices, moving_averages_20_day, moving_averages_4_day, real_time = finnhub_data.get_sma_data()

    # HTML string representation of a plotly chart
    sma_chart = plotly_charts.build_sma(closing_prices, moving_averages_20_day, moving_averages_4_day, real_time)

    # serialize and return a DRF Response
    serialized_data = HTMLChartPlotlySerializer({"chart": sma_chart})

    return Response(serialized_data.data)


@api_view()
def get_recommendation_chart(request):
    """
    Returns a DRF Response with a serialized html string representing a Plotly chart
    """

    recommendation_data = finnhub_data.get_recommendation_data()

    # HTML string representation of a plotly chart
    recommendation_chart = plotly_charts.build_recommendation(recommendation_data)

    # serialize and return a DRF Response
    serialized_data = HTMLChartPlotlySerializer({"chart": recommendation_chart})

    return Response(serialized_data.data)

@api_view()
def get_news_package(request):
    """
    Returns a DRF Response with a serialized dictionary of news data
    """
    raw_news_data = finnhub_data.get_news_data()

    news_package = finnhub_data.create_news_package(raw_news_data)

    serialized_data = NewsDataSerializer({'news': news_package})

    # print(serialized_data.data)

    return Response(serialized_data.data)
