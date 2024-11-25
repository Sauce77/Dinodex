from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Foro(models.Model):
    """
        Modelo utilizado para declarar un foro en la plataforma.
    """
    id_foro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, default="Nuevo Foro")
    descripcion = models.CharField(max_length=600, null=True, blank=True)
    participantes = models.ManyToManyField(User)

    def __str__(self):
        return self.nombre


class Mensaje(models.Model):
    """
        Modelo utilizado para mostrar los mensajes en cada foro.
    """
    id_mensaje = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, default="Nuevo mensaje")
    mensaje = models.CharField(max_length=600)
    foro = models.ForeignKey(Foro, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo
