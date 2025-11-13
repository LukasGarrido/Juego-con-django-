import cv2
from juego.models import Personaje, Pared
import numpy as np

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
    return

