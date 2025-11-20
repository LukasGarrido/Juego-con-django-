from django.shortcuts import render, redirect
from .models import Pared, Personaje
from juego.generar_juego.jugando import generar_pared, generar_fondo, generar_personaje
# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def juego(request):
    generar_pared()
    personajes = generar_personaje()

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

    personaje = Personaje.objects.first()

    personaje_dict = {
        "nombre": personaje.nombre,
        "imagen": personaje.imagen,
        "x": personaje.x,
        "y": personaje.y
    }

    return render(request, "juego.html", {
        'paredes': paredes,
        'personaje': personaje_dict
    })
