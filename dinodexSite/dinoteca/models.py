from django.db import models

# Create your models here.


class Periodo(models.Model):
    id_periodo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    inicio = models.FloatField()
    fin = models.FloatField()

    def __str__(self):
        return self.nombre


class Alimentacion(models.Model):
    """
        Detalla la alimentacion de un dinosaurio.
    """
    id_alimentacionm = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='source/alimento/')

    def __str__(self):
        return self.nombre


class Dinosaurio(models.Model):
    """
        Almacena la informacion de los dinosaurios.
    """
    id_dinosaurio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    tamano = models.FloatField()
    imagen = models.ImageField(upload_to="source/dinosaurio")
    descripcion = models.CharField(max_length=500)
    audio_rugido = models.FileField(upload_to="source/rugido")
    alimenatacion = models.ForeignKey(
        Alimentacion, on_delete=models.DO_NOTHING)
    periodo = models.ForeignKey(Periodo, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre
