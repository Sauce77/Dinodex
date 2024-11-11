from django.shortcuts import render, HttpResponse

from .models import Dinosaurio
# Create your views here.


def userCatalogo(response):
    """
        Muestra todos los dinosaurios de la base
        de datos.
    """
    return HttpResponse("Muchos dinosaurios")
