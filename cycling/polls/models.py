from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
