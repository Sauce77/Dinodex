from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Perfil(models.Model):
    """
        Utilizado para asignar los privilegios de cada
        usuario.
    """
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    visible = models.BooleanField(default=True)
    usuario = models.ManyToManyField(User)

    def __str__(self):
        return self.nombre
