from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from dinoteca.models import Dinosaurio
from .forms import FormEditarDinosaurio, FormEditarCatalogo


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
            nombre = response.POST.get('nombre')
            print("editar:", nombre)
            response.session['nombre_editar'] = nombre
            return redirect('editorEditarDino')
        if boton_eliminar == 'Eliminar':
            # si el valor es Eliminar
            nombre = response.POST.get('nombre')
            print("eliminar:", nombre)
            response.session['nombre_eliminar'] = nombre
            return redirect('editorEliminarDino')
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
        formulario = FormEditarCatalogo(
            initial={'nombre': objeto.nombre})
        # obtenemos la imagen del dinosaurio
        imagen = objeto.imagen
        # lo agregamos a la lista info
        list_info_dino.append(
            {'form': formulario, 'imagen': imagen})
    return render(response, 'editorCatalogoDino.html', {'dinosaurios': list_info_dino, 'usuario': response.user})


def editorEditarDino(response):
    """
        Vista utilizada para modificar un registro de dinosaurio en
        especifico.
    """
    # se obtiene el nombre del registro a editar
    nombre = response.session.get('nombre_editar')
    # se obtiene el objeto a editar
    obj_dino = Dinosaurio.objects.get(nombre=nombre)

    if response.method == "POST":
        # en caso de que tenga peticion post
        form = FormEditarDinosaurio(response.POST, instance=obj_dino)
        if form.is_valid():
            form.save()
            return redirect("editorCatalogo")
    else:
        # se realiza un form con la informacion del objeto
        form = FormEditarDinosaurio(instance=obj_dino)
    return render(response, 'editorEditarDino.html', {'form': form, 'usuario': response.user})


def editorEliminarDino(response):
    """
        Borra el registro elegido por medio de la sesion.
    """
    # obtenemos el nombre
    nombre = response.session.get('nombre_eliminar')
    obj_dino = Dinosaurio.objects.get(nombre=nombre)
    obj_dino.delete()
    return redirect('editorCatalogo')


def editorAgregarDino(response):
    """
        Agrega un registro de dinosaurios.
    """
    if response.method == "POST":
        # en caso de que tenga peticion post
        form = FormEditarDinosaurio(response.POST, response.FILES)
        if form.is_valid():
            form.save()
            return redirect("editorCatalogo")
    else:
        form = FormEditarDinosaurio()
    return render(response, 'editorEditarDino.html', {'form': form, 'usuario': response.user})
