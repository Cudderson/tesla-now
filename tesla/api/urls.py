from django.urls import path
from . import views

# these patterns are imported by parent urls.py 
urlpatterns = [
  path('current-price/', views.get_current_price, name='current-price'),
  path('candlestick/', views.get_candlestick_chart, name='candlestick'),
  path('eps/', views.get_EPS_chart, name='eps'),
  path('sma/', views.get_SMA_chart, name='sma'),
  path('recommendations/', views.get_recommendation_chart, name='recommendations'),
  path('news/', views.get_news_package, name='news')
]