from django.shortcuts import render
import requests

API_KEY = "64dde4abd1244bf49f5d86b83ac922ad"

def home(request):
    country = request.GET.get('country')
    if country:
        query = f"tesla AND {country}"
    else:
        query = "tesla"

    url = f"https://newsapi.org/v2/everything?q={query}&from=2024-05-20&sortBy=publishedAt&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'articles': articles,
        'country': country,
    }
    return render(request, 'news_api/home.html', context)
