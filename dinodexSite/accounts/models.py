from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User

# Create your models here.


class Perfil(models.Model):
    """
        Utilizado para asignar los privilegios de cada
        usuario.
    """
    id_perfil = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)
    descripcion = models.CharField(max_length=250)
    visible = models.BooleanField(default=True)
    usuario = models.ManyToManyField(User)
    imagen = models.ImageField(null=True, blank=True, upload_to="perfiles/")

    def __str__(self):
        return self.nombre


@receiver(post_delete, sender=Perfil)
def eliminar_imagen_producto(sender, instance, **kwargs):
    if instance.imagen:
        instance.imagen.delete(False)
