from django.shortcuts import render
from django.views.generic import TemplateView
from .scraper_provider import ScraperProvider

# Se implementa la vista de noticias utilizando la clase ScraperProvider aplicando el patrón de diseño de factory method de python
class NewsView(TemplateView):
    template_name = 'news.html'
    
    def get(self, request):
        source = request.GET.get('source')
        provider = ScraperProvider()
        # Se obtiene la instancia del scraper correspondiente al origen de noticias
        scraper = provider.get_instance(source)
        headlines = scraper.get_headlines()
        context = {
            'headlines': headlines,
            'source': source
        }
        return render(request, self.template_name, context)