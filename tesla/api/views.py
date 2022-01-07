# api views for rest framework

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import HelloWorldSerializer

@api_view()
def hello_world(request):
    
    data = {"message": "Hello from Django Rest Framework!"}
    results = HelloWorldSerializer(data).data

    return Response(results)
    