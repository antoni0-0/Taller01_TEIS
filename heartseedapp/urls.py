from django.urls import path
from .views import HeartSeedView, MainWallView

urlpatterns = [
    path('', HeartSeedView.as_view(), name='index'),
    path('mainwall/', MainWallView.as_view(), name='mainwall'),
]