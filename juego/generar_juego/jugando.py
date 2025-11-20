import cv2
from juego.models import Personaje, Pared
import numpy as np
import random 
def generar_fondo():
    fondo = np.ones((1000, 1500, 3), dtype=np.uint8) * 255
    return fondo

def generar_pared():
    Pared.objects.all().delete()
    coordenadas = [
        ((50, 100), (1200, 100), 'H'),  #horizontal 1 
        ((50, 300), (900, 300), 'H'),  # horizontal 2
        ((1200, 100), (1200, 700), 'V'),  #vertical 1 
        ((900, 300), (900, 500), 'V'),  #vertical 2
        ((900,500), (50,500), 'V'), #horizontal 3
        ((1200,700), (50,700), 'H'), #horizontal 4
    ]
    
    fondo = np.ones((800, 1500, 3), dtype=np.uint8) * 255

    for i, f, dirc in coordenadas:
        inicio_str = f"{i[0]},{i[1]}"
        final_str = f"{f[0]},{f[1]}"
        Pared.objects.create(inicio=inicio_str, final=final_str, direccion=dirc)
    
    for _ in range(25):

        # dirección al azar
        direccion = random.choice(['H', 'V'])

        if direccion == 'H':
            x1 = random.randint(60, 1150)
            y1 = random.randint(120, 680)
            largo = random.randint(50, 200)
            x2 = x1 + largo
            y2 = y1
        else:
            x1 = random.randint(60, 1150)
            y1 = random.randint(120, 680)
            largo = random.randint(50, 200)
            x2 = x1
            y2 = y1 + largo

        # crear pared
        Pared.objects.create(
            inicio=f"{x1},{y1}",
            final=f"{x2},{y2}",
            direccion=direccion
        )


def generar_personaje():
    nombre_personaje = "personaje1"
    ruta = "/static/img/devil.png"
    x = 100
    y = 100
    Personaje.objects.all().delete()
    return Personaje.objects.create(nombre = nombre_personaje, imagen= ruta, x = x, y = y)


def mover_personaje(personaje, dx, dy):
    
    nuevo_x = personaje.x + dx
    nuevo_y = personaje.y + dy

    # límites del canvas
    min_x = 0
    max_x = 1450
    min_y = 0
    max_y = 750

    if nuevo_x < min_x: nuevo_x = min_x
    if nuevo_x > max_x: nuevo_x = max_x
    if nuevo_y < min_y: nuevo_y = min_y
    if nuevo_y > max_y: nuevo_y = max_y

    personaje.x = nuevo_x
    personaje.y = nuevo_y
    personaje.save()

    return personaje
