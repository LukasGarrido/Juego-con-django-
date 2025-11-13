from django.db import models

# Create your models here.

class Personaje(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="personajes/")
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} con posicion ({self.x},{self.y})"

class Pared(models.Model):
    inicio = models.CharField(max_length=10)
    final = models.CharField(max_length=10)
    direccion = models.CharField(max_length=1) #H , V
    color = models.CharField(max_length=15, default='0,0,0')

    def __str__(self):
        return f"Pared iniciada en {self.inicio} con final en {self.final}, con una direccion {self.direccion}"
