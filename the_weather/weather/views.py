from django.shortcuts import render
import requests
from .models import City
from .forms import *

# Create your views here.

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'


    city = 'Las Vegas'

    form = CityForm()

    cities = City.objects.all()

    if request.method == 'POST':   # only true if form is submitted
        form = CityForm(request.POST)   # add actual request data to form for processing
        form.save()                         # will validate and save if validate

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

 

    context = {'weather_data':weather_data,'form':form}

    return render (request,'weather/index.html',context)
