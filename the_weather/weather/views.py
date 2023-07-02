from django.shortcuts import render
import requests

# Create your views here.

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'


    city = 'Las Vegas'

    api_key = ''

    city_weather = requests.get(url.format(city, api_key)).json()

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    context = {'weather':weather}

    return render (request,'weather/index.html',context)
