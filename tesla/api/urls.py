from django.urls import path
from . import views

# these patterns are imported by parent urls.py 
urlpatterns = [
  path('hello-world/', views.hello_world, name='hello-world'),
  path('test-current-price/', views.test_get_current_price, name='test-current-price'),
  path('test-get-candlestick', views.get_candlestick_chart, name='test-get-candlestick'),
]