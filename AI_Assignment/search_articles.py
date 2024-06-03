import requests
from bs4 import BeautifulSoup

def search_health_articles(analysis):
    query = " health recommendations"
    url = f"https://www.google.com/search?q={query}"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    for item in soup.find_all('h3'):
        articles.append(item.get_text())

    return articles[:5]  # Return top 5 articles
