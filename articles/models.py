from django.db import models

# Create your models here.

class Restaurantes(models.Model):
    nombre = models.CharField(max_length=50)
    cocina = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()

class Bares(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    
class Clientes(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    es_huesped=models.BooleanField()
    habitacion=models.IntegerField()
    numero_telefono=models.IntegerField()
