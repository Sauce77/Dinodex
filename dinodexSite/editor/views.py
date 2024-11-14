from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from dinoteca.models import Dinosaurio
from .forms import FormEditarDinosaurio


def editorInicio(response):
    return HttpResponse("Bienvenido Editor!")


def editorCatalogo(response):
    """
        Muestra el catalogo completo de dinosaurios,
        puede selccionar uno y editar. Tambien puede
        borrar y anadir nuevos.
    """
    if response.method == 'POST':
        # si se recibe peticion POST
        boton_editar = response.POST.get('editar')
        boton_eliminar = response.POST.get('eliminar')

        if boton_editar == 'Editar':
            # si el valor es Editar
            id_dino = response.POST.get('id_dinosaurio')
            print("editar ID:", id_dino)
            response.session['id_dino'] = id_dino
            return redirect('editorEditaDino')
        if boton_eliminar == 'Eliminar':
            # si el valor es Eliminar
            id_dino = response.POST.get('id_dinosaurio')
            print("eliminar ID:", id_dino)
            return HttpResponse("Borra eso William")
        else:
            # en caso de que no
            return HttpResponse('Ha sucedido un error')

    # obtenemos todos los dinosaurios
    obj_dinosaurio = Dinosaurio.objects.all()

    # realizamos un form para cada dinosaurio
    list_info_dino = []
    for objeto in obj_dinosaurio:
        # para cada dinosaurio
        # se obtiene el id del dinosaurio
        formulario = FormEditarDinosaurio(
            initial={'id_dinosaurio': objeto.id_dinosaurio})
        # obtenemos el nombre del dinosaurio
        nombre = objeto.nombre
        # obtenemos la imagen del dinosaurio
        imagen = objeto.imagen
        # lo agregamos a la lista info
        list_info_dino.append(
            {'form_id': formulario, 'nombre': nombre, 'imagen': imagen})
    return render(response, 'editorCatalogoDino.html', {'dinosaurios': list_info_dino, 'usuario': response.user})


def editorEditaDino(response):
    """
        Vista utilizada para modificar un registro de dinosaurio en
        especifico.
    """
    pk = response.session.get('editar_id_dino')
    obj_dino = Dinosaurio.objects.get(pk=pk)
    form = FormEditarDinosaurio(instance=obj_dino)
    return render(response, 'editorEditaDino.html', {'form': form, 'usuario': response.user})
