from django.shortcuts import render, HttpResponse

# Create your views here.
from dinoteca.models import Dinosaurio
from .forms import FormDinosaurio


def editorInicio(response):
    return HttpResponse("Bienvenido Editor!")


def editorCatalogo(response):
    """
        Muestra el catalogo completo de dinosaurios,
        puede selccionar uno y editar. Tambien puede
        borrar y anadir nuevos.
    """
    # obtenemos todos los dinosaurios
    obj_dinosaurio = Dinosaurio.objects.all()

    # realizamos un form para cada dinosaurio
    list_info_dino = []
    for objeto in obj_dinosaurio:
        # para cada dinosaurio
        # se obtiene el id del dinosaurio
        formulario = FormDinosaurio(
            initial={'id_dinosaurio': objeto.id_dinosaurio})
        # obtenemos el nombre del dinosaurio
        nombre = objeto.nombre
        # obtenemos la imagen del dinosaurio
        imagen = objeto.imagen
        # lo agregamos a la lista info
        list_info_dino.append(
            {'form_id': formulario, 'nombre': nombre, 'imagen': imagen})
    return render(response, 'editorCatalogoDino.html', {'dinosaurios': list_info_dino, 'usuario': response.user})
