---
<div align='center'>
  
  # Tesla Now
  
  ### Real-time charts, trends, and news for Tesla Inc.
  <img src='https://img.shields.io/badge/Tesla Now-online-brightgreen'>
  
  ### Live: [https://tesla-now.netlify.app/](https://tesla-now.netlify.app/)
</div>

---

<!-- =============================
<br><br><br><br><br><br><br><br><br><br>
 -->
 <br>

![tesla-now-1.png](https://github.com/Cudderson/tesla-now/blob/master/tesla-now-1.png)

<br>

## About 

### Tesla Now is a web application that uses real-time data to provide users with interactive charts, statistics, and Tesla-related news/articles --as soon as they're published.

<br>

## Built With
- ReactJS
- Django/Python
- Plotly

<br>

## Content/Usage
#### This site offers the following content, constructed with real-time Tesla data:
  - Candlestick Chart (OHLC)
  - Earnings Per Share Chart
  - Moving Averages Chart
  - Analyst Buy/Sell Recommendations Chart
  - News Page

<br>

### Notes:
  - #### *New data is retrieved every 5 minutes, and site content will update automatically. No need to refresh the page.*
  - #### *Double-tap on a chart to restore it to its original state.*

<!-- ## Usage

- Running this project locally will require a little extra work, as you will need your own assets/keys:
  - A Free API key from http://finnhub.io
  - A Django 'SECRET_KEY'
    - from https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/ : 
  
  `
  'The secret key must be a large random value and it must be kept secret.'
  `
### 1. Set Environment Variables
- For privacy, the keys are not stored within the project's files. Instead, save them as environment variables on your os.
- 'settings.py' uses `os.getenv()` to retrieve the keys from your system variables:

```
SECRET_KEY = os.getenv('SECRET_KEY')

FINN_KEY = os.getenv('FINN_KEY')
```
Create environment variables with names `SECRET_KEY` and `FINN_KEY`, with values set to your Django key and Finnhub API key.
  - How to set environment variables: https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html

### 2. pip install requirements
  - (virtual environment active preferred) In terminal, navigate to project directory:
  `cd tesla_now`
  and pip install the requirements:
  `pip install -r requirements.txt`
  
### 3. Run Local Server
  - Still in terminal, navigate back to the previous directory `cd ..` and run `python manage.py runserver`
  - Project should now be running on your local server: `http://127.0.0.1:8000/`
  -->

<br>

### Author

- #### Cody : Myself
- #### Contact me for anything related to this project, programming, or hiring: 
  - #### email: codered1227@gmail.com
