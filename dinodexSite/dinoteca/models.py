from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.


class Periodo(models.Model):
    """
        Identifica los diferentes periodos de la prehistoria.
    """
    id_periodo = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    descripcion = models.CharField(max_length=500)
    inicio = models.FloatField()
    fin = models.FloatField()

    def __str__(self):
        return self.nombre


class Alimentacion(models.Model):
    """
        Detalla la alimentacion de un dinosaurio.
    """
    id_alimentacion = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(null=True, blank=True, upload_to='alimento/')

    def __str__(self):
        return self.nombre


class Dinosaurio(models.Model):
    """
        Almacena la informacion de los dinosaurios.
    """
    id_dinosaurio = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=150)
    tamano = models.FloatField()
    imagen = models.ImageField(null=True, blank=True, upload_to="dinosaurio/")
    descripcion = models.CharField(max_length=500)
    audio_rugido = models.FileField(upload_to="rugido/")
    alimentacion = models.ForeignKey(
        Alimentacion, on_delete=models.DO_NOTHING)
    periodo = models.ForeignKey(Periodo, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre


@receiver(post_delete, sender=Dinosaurio)
def eliminar_imagen_producto(sender, instance, **kwargs):
    if instance.imagen:
        instance.imagen.delete(False)
