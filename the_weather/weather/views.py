from django.shortcuts import render
import requests
from .models import City

# Create your views here.

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'


    city = 'Las Vegas'

    cities = City.objects.all()

    api_key = ''

    weather_data = []

    for city in cities:
           
           city_weather = requests.get(url.format(city, api_key)).json()

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    weather_data.append(weather) 

 

    context = {'weather_data':weather_data}

    return render (request,'weather/index.html',context)
