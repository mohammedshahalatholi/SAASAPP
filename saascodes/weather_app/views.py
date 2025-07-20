import requests
from django.shortcuts import render

def weather_dashboard(request):
    api_key = "e6b21cb29795c0f20c86031e2281ccca"  # Keep this secure, preferably in environment variables or Django settings
    city = request.GET.get('city', 'Nairobi')  # Default city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        context = {
            'city': city,
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
        }
    else:
        context = {'error': 'City not found. Please try again.'}
    
    return render(request, 'static/weather_dashboard.html', {'context':context})
