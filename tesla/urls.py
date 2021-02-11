""" Defines URL patterns for 'tesla' """

from django.urls import path

from . import views

app_name = 'tesla'
urlpatterns = [
    # Initial landing page
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('eps/', views.eps, name='eps'),
    path('sma/', views.sma, name='sma'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('news/', views.news, name='news'),
]
