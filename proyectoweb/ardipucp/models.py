from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=64, default='')
    local = models.CharField(max_length=64, default='')
    codigo_usuario = models.CharField(max_length=64, default='')
    clave = models.CharField(max_length=64, default='')

class productos(models.Model):
    categoria = models.CharField(max_length=64, default='')
    producto = models.CharField(max_length=100, default='')
    imagen = models.CharField(max_length=64, default='')
    precio = models.CharField(max_length=64, default='')
    stock = models.CharField(max_length=64, default='')
    descripcion = models.CharField(max_length=200, default='')
