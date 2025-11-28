import cv2
from juego.models import Personaje, Pared, Villano
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
    nombre_personaje = "batman"
    ruta = "/static/img/batman.png"
    x = 100
    y = 100
    Personaje.objects.all().delete()
    return Personaje.objects.create(
        nombre = nombre_personaje, 
        imagen= ruta, 
        x = x, 
        y = y
        )

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

#Funciones del personaje villano 
def generar_villano():
    list_villanos = ["acertijo.png", "doscaras.png", "joker.png"]
    villanos_creados = []

    Pared.objects.all().delete()
    generar_pared()  

    paredes = list(Pared.objects.all())

    Villano.objects.all().delete()

    for v in list_villanos:
        nombre_villano = v.split(".")[0]
        ruta_villano = "/static/img/" + v
        #loop para que el villano no se genere en la misma posicion que una pared.
        while True:
            X = random.randint(100, 1700)
            Y = random.randint(100, 900)
            choque = False
            for p in paredes:
                x1, y1 = map(int, p.inicio.split(","))
                x2, y2 = map(int, p.final.split(","))
                grosor = 20  
                if p.direccion == "H":
                    if (X < x2 and X+50 > x1) and (Y < y1+grosor and Y+50 > y1):
                        choque = True
                        break
                else:  
                    if (Y < y2 and Y+50 > y1) and (X < x1+grosor and X+50 > x1):
                        choque = True
                        break
            if not choque:
                break

        villano = Villano.objects.create(
            nombre=nombre_villano,
            imagen=ruta_villano,
            x=X,
            y=Y
        )
        villanos_creados.append(villano)

    return villanos_creados
