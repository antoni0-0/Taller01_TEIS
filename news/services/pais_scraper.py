from .base_scraper import NewsScraper
import requests
from bs4 import BeautifulSoup

# Se implementa el scraper de noticias específico para El País utilizando la clase abstracta
class PaisScraper(NewsScraper):
    def get_headlines(self):
        page = requests.get('https://elpais.com/noticias/medio-ambiente/')
        soup = BeautifulSoup(page.text, 'html.parser')
        news = soup.find_all('article')
        print(news[0])
        
        pais_news = []
        for i in range(10):
            img = str(news[i].find('img').get('src'))
            title = news[i].find('h2').find('a').text
            link =str(news[i].find('figure').find('a').get('href'))
            pais_news.append({
                'title': title,
                'link': link,
                'img': img
            })
        return pais_news