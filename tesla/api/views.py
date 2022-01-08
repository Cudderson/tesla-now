# api views for rest framework

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import HelloWorldSerializer, PriceSerializer

# maybe move these?
import os
finn_key = os.getenv('FINN_KEY')
import requests

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
