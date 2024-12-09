from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import random
import string


def generar_codigo_alfanumerico(longitud=15):
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(random.choice(caracteres) for _ in range(longitud))
    return codigo


class Foro(models.Model):
    """
        Modelo utilizado para declarar un foro en la plataforma.
    """
    id_foro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, default="Nuevo Foro")
    descripcion = models.CharField(max_length=600, null=True, blank=True)
    participantes = models.ManyToManyField(User)
    codigo = models.CharField(max_length=15, default="No-code")

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


@receiver(post_save, sender=Foro)
def create_unique_code(sender, instance, created, **kwargs):
    if created:
        instance.codigo = generar_codigo_alfanumerico()
        instance.save()
