from django.urls import path
from .views import inicio, juego

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('juego/',juego, name="juego")
]