from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=64, default='')
    local = models.CharField(max_length=64, default='')
    codigo_usuario = models.CharField(max_length=64, default='')
    clave = models.CharField(max_length=64, default='')