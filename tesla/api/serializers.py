# serializers for rest framework apis
from rest_framework import serializers

class HelloWorldSerializer(serializers.Serializer):
    '''Your data serializer, define your fields here'''

    message = serializers.CharField(max_length=100)

class PriceSerializer(serializers.Serializer):
    '''serialize current price data for react'''

    price = serializers.DictField()

# serialize a plotly figure (already in html format)
class HTMLChartPlotlySerializer(serializers.Serializer):
    """
    Serializes a Plotly Figure that was converted to HTML (plotly.graph_objs.Figure.to_html())
    """

    # apparently, the .to_html() method converts our chart into a an HTML div string.
    # let's first just retrieve said string

    chart = serializers.CharField()
