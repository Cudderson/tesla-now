from django.shortcuts import render

from . import tesla_utils

# Create your views here.


def landing(request):
    """The initial landing page for Tesla Now"""

    welcome_text = "Welcome to Tesla Now."

    description = "Real-time charts, news, and opinions all in one place."

    context = {'greeting': welcome_text, "description": description}

    return render(request, 'tesla/landing.html', context)


def home(request):
    """The Home/Main page of Tesla One"""
    # First step is generating a tesla chart
    # This view should provide data to template only, not calculate/generate chart
    current_price = tesla_utils.current_price()

    context = {'current_price': current_price}

    return render(request, 'tesla/home.html', context)
