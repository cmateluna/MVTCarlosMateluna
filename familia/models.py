from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
