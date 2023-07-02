from django.shortcuts import render
import requests

# Create your views here.

def index(requests):
    return render (requests,'weather/index.html')
