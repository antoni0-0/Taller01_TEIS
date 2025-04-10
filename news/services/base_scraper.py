from abc import ABC, abstractmethod


#Se define una interfaz abstracta para los scrapers de noticias
class NewsScraper(ABC):
    @abstractmethod
    def get_headlines(self):
        pass