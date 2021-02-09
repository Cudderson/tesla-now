"""This file will contain utilities that our view functions can use"""

# First goal: a utility that generates a real-time chart for our view to use.

# Finnhub 'quote' !!!

# the best way i can think of to do this would be:
# create a candlestick chart of the last month (or what is appropriate) of tesla.
# above/below that, I can display the current price of Tesla, and maybe a %up or %down figure

# let's start by displaying the current price of tesla on the page, by creating a function that returns
# the current Tesla price to our view function, which will pass to the template

import requests
import config


def current_price():
    """returns the current price of Tesla"""

    r = requests.get(f'https://finnhub.io/api/v1/quote?symbol=TSLA&token={config.my_key}')
    res = r.json()

    return res['c']
