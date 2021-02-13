from django.shortcuts import render

from . import tesla_utils


def landing(request):
    """The initial landing page for Tesla Now"""

    welcome_text = "Welcome to Tesla Now."

    description = "View Tesla-specific charts, news, and analyst recommendations, all in real-time."

    context = {'greeting': welcome_text, "description": description}

    return render(request, 'tesla/landing.html', context)


def home(request):
    """The Home/Main page of Tesla One"""
    # First step is generating a tesla chart
    # This view should provide data to template only, not calculate/generate chart
    current_price = tesla_utils.current_price()
    home_chart = tesla_utils.create_candle_chart()

    context = {'current_price': current_price, 'home_chart': home_chart}

    return render(request, 'tesla/home.html', context)


def eps(request):
    """Page that displays an EPS chart for Tesla"""

    eps_chart = tesla_utils.create_eps_chart()

    context = {'eps_chart': eps_chart}

    return render(request, 'tesla/eps.html', context)


def sma(request):
    """Page that displays a 20-day sma chart for Tesla"""

    sma_chart = tesla_utils.create_sma_chart()

    context = {'sma_chart': sma_chart}

    return render(request, 'tesla/sma.html', context)


def recommendations(request):
    """Page that displays analyst recommendations for Tesla"""

    recommend_chart = tesla_utils.create_recommend_chart()

    context = {'recommend_chart': recommend_chart}

    return render(request, 'tesla/recommend.html', context)


def news(request):
    """Page that displays newest news articles for Tesla"""

    news_package = tesla_utils.create_news_package()

    context = {'news_package': news_package}

    return render(request, 'tesla/news.html', context)
