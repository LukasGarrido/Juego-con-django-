import cv2
from juego.models import Personaje, Pared
import numpy as np
import random 
def generar_fondo():
    fondo = np.ones((1000, 1500, 3), dtype=np.uint8) * 255
    return fondo

def generar_pared():
    coordenadas = [
        ((50, 100), (1200, 100), 'H'),  #horizontal 1 
        ((50, 300), (900, 300), 'H'),  # horizontal 2
        ((1200, 100), (1200, 700), 'V'),  #vertical 1 
        ((900, 300), (900, 500), 'V'),  #vertical 2
        ((900,500), (50,500), 'V'), #horizontal 3
        ((1200,700), (50,700), 'H'), #horizontal 4
    ]
    Pared.objects.all().delete()

    fondo = np.ones((800, 1500, 3), dtype=np.uint8) * 255

    for i, f, dirc in coordenadas:
        inicio_str = f"{i[0]},{i[1]}"
        final_str = f"{f[0]},{f[1]}"
        Pared.objects.create(inicio=inicio_str, final=final_str, direccion=dirc)


def generar_personaje():
    nombre_personaje = "personaje1"
    ruta = "/static/img/devil.png"
    x = 100
    y = 100
    Personaje.objects.all().delete()
    return Personaje.objects.create(nombre = nombre_personaje, imagen= ruta, x = x, y = y)

"""
    def movimiento_ilimitado(self, key, fondo):
        if key == ord('d'):
            self.x += self.velocidad
        elif key == ord('a'):
            self.x -= self.velocidad
        elif key == ord('w'):
            self.y -= self.velocidad
        elif key == ord('s'):
            self.y += self.velocidad
"""
def mover_personaje(personaje, key, fondo):
    if key == ord('d'):
        personaje.x += personaje.velocidad
    elif key == ord('a'):
        personaje.x -= personaje.velocidad
    elif key == ord('w'):
        personaje.y -= personaje.velocidad
    elif key == ord('s'):
        personaje.y += personaje.velocidad
    
    x, y = fondo.shape[:2]

    x_min = 50
    x_max = x - personaje.ancho
    y_min = 100
    y_max = y - personaje.alto