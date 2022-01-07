# serializers for rest framework apis
from rest_framework import serializers

class HelloWorldSerializer(serializers.Serializer):
    '''Your data serializer, define your fields here'''

    message = serializers.CharField(max_length=100)