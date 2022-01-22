# serializers for rest framework apis
from rest_framework import serializers

# saving as examples for now
# class HelloWorldSerializer(serializers.Serializer):
#     '''Your data serializer, define your fields here'''

#     message = serializers.CharField(max_length=100)

# class PriceSerializer(serializers.Serializer):
#     '''serialize current price data for react'''

#     price = serializers.DictField()


class PriceSerializer(serializers.Serializer):
    """
    Serializes a floating point number
    """

    current_price = serializers.FloatField()

# serialize a plotly figure (already in html format)
class HTMLChartPlotlySerializer(serializers.Serializer):
    """
    Serializes a Plotly Figure that was converted to HTML for consumption by React
    unserialized html format: chart = plotly.offline.plot(fig, include_plotlyjs=False, output_type="div")
    """

    # using CharField for now, may change to DictField/JSONField
    chart = serializers.CharField()

# serialize our news data
class NewsDataSerializer(serializers.Serializer):
    """
    Serializes news data (text, links, images) from finnhub api
    """

    news = serializers.JSONField()