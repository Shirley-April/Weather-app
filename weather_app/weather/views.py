from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c60582c47fe785a56ebd2ac8d0e51e78'
  
    city = 'Nairobi'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()


    cities = City.objects.all()

    for city in cities:

        weather_data = []

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r["main"]["temp"],
            'description': r["weather"][0]["description"],
            'icon': r["weather"][0]["icon"],
        }

        weather_data.append(city_weather)


    context = {'weather_data' : weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)