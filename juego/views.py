from django.shortcuts import render, redirect
from .models import Pared, Personaje
from juego.generar_juego.jugando import generar_pared
# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def juego(request):
    generar_pared()
    paredes = []
    for pared in Pared.objects.all():
        x1, y1 = map(int, pared.inicio.split(','))
        x2, y2 = map(int, pared.final.split(','))
        paredes.append({
            'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2,
            'direccion': pared.direccion
        })
    return render(request, 'juego.html', {'paredes': paredes})
