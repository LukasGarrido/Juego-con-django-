from django.shortcuts import render, redirect
from .models import Pared, Personaje, Villano
from juego.generar_juego.jugando import generar_pared, generar_personaje, generar_villano
# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def juego(request):
    generar_pared()
    personajes = generar_personaje()
    villanos = generar_villano()
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
    villanos_list = []
    for villano in Villano.objects.all():
        villanos_list.append(villano)

    personaje = Personaje.objects.first()
    personaje_dict = {
        "nombre": personaje.nombre,
        "imagen": personaje.imagen,
        "x": personaje.x,
        "y": personaje.y,
        "velocidad": personajes.velocidad
    }

    return render(request, "juego.html", {
        'paredes': paredes,
        'personaje': personaje_dict,
        'villanos': villanos_list,
    })
