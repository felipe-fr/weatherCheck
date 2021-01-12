from django.http import HttpResponse, JsonResponse
import requests

def get_weather(name):
    API_KEY = "b77e07f479efe92156376a8b07640ced"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()


def index(request):
    r = get_weather("London")
    return JsonResponse(r)