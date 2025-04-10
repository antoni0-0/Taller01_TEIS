import requests
from .base_scraper import NewsScraper
from bs4 import BeautifulSoup

# Se implementa el scraper de noticias específico para BBC utilizando la clase abstracta
class BBCScraper(NewsScraper):
    def get_headlines(self):
        page = requests.get('https://www.bbc.com/mundo/topics/cjgn709jk16t')
        soup = BeautifulSoup(page.text, 'html.parser')
        news = soup.find_all(class_="bbc-l5xv05 e1v051r10")
        
        bbc_news = []
        for i in range(10):
            img = str(news[i].find('img').get('src'))
            title = str(news[i].find('a').text)
            link = str(news[i].find('a').get('href'))
            bbc_news.append({
                'title': title,
                'link': link,
                'img': img
            })
        return bbc_news