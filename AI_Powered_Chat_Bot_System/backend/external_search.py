import requests
from bs4 import BeautifulSoup

class ExternalSearch:
    def perform_search(self, query):
        response = requests.get(f'https://www.google.com/search?q={query}')
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('h3')
        return search_results
