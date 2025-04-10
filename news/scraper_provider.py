from .services.bbc_scraper import BBCScraper
from .services.pais_scraper import PaisScraper

# Se implementa el proveedor de scrapers para obtener instancias de scrapers específicos (inyector de depencencias)
class ScraperProvider:
    def get_instance(self, source):
        if source == 'bbc':
            return BBCScraper()
        elif source == 'pais':
            return PaisScraper()
        else:
            raise ValueError("Unknown source")