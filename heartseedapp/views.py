from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# Se implementan las vistas utilizando el patrón de diseño CBV de Django sin redefinir el método get
class HeartSeedView(TemplateView):
    template_name = 'index.html'
    
class MainWallView(TemplateView):
    template_name = 'main-wall.html'