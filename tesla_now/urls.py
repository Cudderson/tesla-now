"""
tesla_now URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include

# api urls
from tesla.api.urls import urlpatterns as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # django frontend (deprecating/replacing with React frontend, may break at any time)
    # path('', include('tesla.urls')),

    # new: only allow '/api' or '/admin' as backend url patterns (can make new basename later)
    # sets 'api/' as the basename for api urls
    path('api/', include(api_urls)),
]
