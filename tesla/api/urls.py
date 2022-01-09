from django.urls import path
from . import views

# these patterns are imported by parent urls.py 
urlpatterns = [
  path('test-get-candlestick', views.get_candlestick_chart, name='test-get-candlestick'),
  path('eps/', views.get_EPS_chart, name='eps'),
  path('sma/', views.get_SMA_chart, name='sma')
]