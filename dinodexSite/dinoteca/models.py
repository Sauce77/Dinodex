from django.db import models

# Create your models here.


class Alimentacion(models.Model):
    """
        Detalla la alimentacion de un dinosaurio.
    """
    id_alimentacionm = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='sources/alimento/imagen')

    def __str__(self):
        return self.nombre
