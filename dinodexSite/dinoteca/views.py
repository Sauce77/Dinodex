from django.shortcuts import render, HttpResponse, redirect

from .models import Dinosaurio
# Create your views here.

from .forms import FormMostrarCatalogo


def userCatalogo(response):
    """
        Muestra el catalogo completo de dinosaurios,
        puede selccionar uno y editar. Tambien puede
        borrar y anadir nuevos.
    """
    if response.method == "POST":
        boton_mirar = response.POST.get('mirar')
        nombre_dino = response.POST.get('nombre')

        if boton_mirar == 'Mirar':
            # si se ha presionado mirar
            response.session['nombre_dino'] = nombre_dino
            return redirect('userMirarDino')

    # obtenemos todos los dinosaurios
    obj_dinosaurio = Dinosaurio.objects.all()

    # realizamos un form para cada dinosaurio
    list_info_dino = []
    list_filas = []
    for index, objeto in enumerate(obj_dinosaurio):
        # para cada dinosaurio
        # se obtiene el id del dinosaurio
        formulario = FormMostrarCatalogo(
            initial={'nombre': objeto.nombre})
        # obtenemos la imagen del dinosaurio
        imagen = objeto.imagen
        # lo agregamos a la lista info
        list_filas.append(
            {'form': formulario, 'imagen': imagen})
        # agrupamos en tres
        if index % 3 == 2 or index == obj_dinosaurio.count() - 1:
            list_info_dino.append(list_filas)
            list_filas = []
    return render(response, 'userCatalogoDino.html', {'dinosaurios': list_info_dino, 'usuario': response.user})


def userMirarDino(response):
    """
        Muestra la informacion del dinosaurio
        seleccionado en el catalogo
    """
    nombre_dino = response.session.get('nombre_dino')
    obj_dino = Dinosaurio.objects.get(nombre=nombre_dino)
    obj_alimento = obj_dino.alimenatacion

    return render(response, 'userMirarDino.html', {'dinosaurio': obj_dino, 'alimento': obj_alimento, 'usuario': response.user})
