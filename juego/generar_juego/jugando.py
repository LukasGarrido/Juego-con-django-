import cv2
from juego.models import Personaje, Pared
import numpy as np
import random 

def generar_fondo():
    fondo = np.ones((1000, 1500, 3), dtype=np.uint8) * 255
    return fondo

#Funciones de las paredes 
def generar_pared():
    Pared.objects.all().delete()
    
    for _ in range(50):
        direccion = random.choice(['H', 'V'])

        if direccion == 'H':
            x1 = random.randint(60, 1700)
            y1 = random.randint(120, 780)
            largo = random.randint(50, 300)
            x2 = x1 + largo
            y2 = y1
        else:
            x1 = random.randint(60, 1700)
            y1 = random.randint(120, 780)
            largo = random.randint(50, 300)
            x2 = x1
            y2 = y1 + largo

        Pared.objects.create(
            inicio=f"{x1},{y1}",
            final=f"{x2},{y2}",
            direccion=direccion
        )

    return Pared.objects.all()

#Funciones del personaje  
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
    max_x = 1920
    min_y = 0
    max_y = 1080

    if nuevo_x < min_x: nuevo_x = min_x
    if nuevo_x > max_x: nuevo_x = max_x
    if nuevo_y < min_y: nuevo_y = min_y
    if nuevo_y > max_y: nuevo_y = max_y

    personaje.x = nuevo_x
    personaje.y = nuevo_y
    personaje.save()

    return personaje
