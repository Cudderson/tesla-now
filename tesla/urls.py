""" Defines URL patterns for 'tesla' """

from django.urls import path

from . import views

app_name = 'tesla'
urlpatterns = [
    # Initial landing page
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
]

