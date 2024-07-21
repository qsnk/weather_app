from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import viewsets
from weather.forms import WeatherForm, LoginForm, SignupForm
from weather.models import City, UserSearchHistory
from weather.serializers import CitySerializer, UserSearchHistorySerializer, UserSerializer
import requests

def index(request):
    if request.method == 'POST':
        weatherForm = WeatherForm(request.POST)

        city_name = request.POST['city']
        city, created = City.objects.get_or_create(name=city_name)
        city.increment_queries_count()
        city.save()

        if request.user.is_authenticated:
            search_history = UserSearchHistory(user=request.user, city=city)
            search_history.save()

        weather_data = {}
        if weatherForm.is_valid():
            geo_location = get_geo_location(city_name).get('results')[0]
            latitude = geo_location.get('latitude')
            longitude = geo_location.get('longitude')
            weather_data = get_weather_data(latitude, longitude)
            context = {
                'city': city_name,
                'weather_data': weather_data,
            }
            return render(request, 'weather.html', context)
    else:
        weatherForm = WeatherForm()
        weather_data = {}
    user = request.user
    context = {
        'user': user,
        'form': weatherForm,
        'data': weather_data
    }
    return render(request, 'index.html', context)

def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 == password2:
                    form.save()
                return redirect('/login/')

    form = SignupForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login/')

def get_geo_location(city: str):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=ru&format=json"
    response = requests.get(url).json()
    return response

def get_weather_data(lat: float, lon: float):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(url).json()
    return response

def api_docs(request):
    return render(request, 'api_docs.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer


class UserSearchHistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user search history to be viewed or edited.
    """
    serializer_class = UserSearchHistorySerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return UserSearchHistory.objects.filter(user=user).order_by('-date_time')
        return UserSearchHistory.objects.none()