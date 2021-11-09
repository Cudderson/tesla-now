## This project is live: 

### http://tesla-now.herokuapp.com

#### ( Allow time for initial load, as this app will likely be cold-starting due to low traffic/requests. Page requests after the inital connection will be quicker. ) 

# About

![tesla-now-1.png](https://github.com/Cudderson/tesla-now/blob/master/tesla-now-1.png)

## Tesla Now is a web application that serves as a central location for all things Tesla. 

### Using real-time data, Tesla Now provides the user with interactive charts, statistics, and Tesla-related news/articles-- as soon as they're published.


## Built With
- Django/Python
- Bootstrap
- Plotly

## Usage

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

## Developer Notes
  - Site is secure via SSL/HTTPS
  - Though this site is fully-responsive, view on desktop for the best user-experince. The plotly charts appear more-congested on mobile. 


## Author

- Cody : Myself
  - This was a fun project to make, and I use it often to check out the newest Tesla articles and watch the candlestick chart evolve. Django is great as well.

- Contact me for anything related to this project, programming, or hiring: - codered1227@gmail.com

Thanks for checking it out. If you enjoyed the project, consider giving it a 'star'! 

*** Tesla Now is a non-monetized project with no affiliation to Tesla Inc. ***
