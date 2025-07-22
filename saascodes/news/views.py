import requests
from django.shortcuts import render

def finance_news(request):
    url = (
        'https://newsapi.org/v2/everything?'
        'q=finance&'
        'apiKey=05f1aaac551b411e94ae3a04e4aa2363'
    )
    response = requests.get(url).json()
    articles = response.get('articles', [])
    return render(request, 'newsarticle.html', {'articles': articles})
