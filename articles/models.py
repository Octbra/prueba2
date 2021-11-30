from django.db import models

# Create your models here.

class Restaurantes(models.Model):
    nombre = models.CharField(max_lenght=100)
    cocina = models.CharField(max_lenght=100)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
  