from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
# Create your views here.
from .models import Foro, Mensaje
from .forms import FormMensaje, FormCrearForo


def forosInicio(response):
    """
        Muestra todos los foros disponibles para el usuario.
    """
    # obtnemos el usuario
    usuario = response.user

    # si se recibe un post
    if response.method == "POST":
        # obtenemos el boton codigo
        btn_registrar = response.POST.get('BotonCodigo')
        # obtenemos el boton foro
        btn_foro = response.POST.get('BotonForo')

        if btn_registrar == "Registrar":
            # obtenemos el codigo
            codigo = response.POST.get('codigo')
            # si el boton es registrar
            obj_usuario = User.objects.get(username=usuario.username)

            if Foro.objects.get(codigo=codigo).exists():
                # si el foro existe
                # obtenemos el objeto del foro
                foro = Foro.objects.get(codigo=codigo)
                # agregamos al usuario como participante
                foro.participantes.add(obj_usuario)
            else:
                return HttpResponse("Codigo de foro invalido")
        if btn_foro == "Foro":
            # si se presiona el boton 'Ir'
            # obtenemos el nombre del foro
            nombre_foro = response.POST.get('foro')
            # guardamos el objeto foro en la respuesta
            response.session['foro'] = nombre_foro
            return redirect('userMostrarForo')

    # se obtienen los foros en los que el usuario participa
    obj_foros = Foro.objects.filter(participantes=usuario)
    return render(response, "forosInicio.html", {'usuario': usuario, 'foros': obj_foros})


def userMostrarForo(response):
    """
        Se muestran todos los mensajes del foro elegido.
    """

    # obtenemos el nombre del foro
    nombre_foro = response.session.get('foro')
    # obtenemos el objeto foro
    obj_foro = Foro.objects.get(nombre=nombre_foro)
    # obtenemos todos los mensajes
    obj_mensaje = Mensaje.objects.filter(foro=obj_foro)
    return render(response, "userMostrarForo.html", {'usuario': response.user, 'foro': obj_foro, 'mensajes': obj_mensaje})


def userAgregarMensaje(response):
    """
        Despliega un formulario para un nuevo mensaje.
    """

    # obtenemos el usuario
    usuario = response.user
    # obtenemos el nombre del foro
    nombre_foro = response.session.get('foro')
    # obtenemos el objeto foro
    obj_foro = Foro.objects.get(nombre=nombre_foro)

    if response.method == 'POST':
        # obtenemos el boton enviar
        btn_enviar = response.POST.get('enviar')

        if btn_enviar == 'Enviar':
            print("si jala")
            # en caso de que tenga peticion post
            form = FormMensaje(response.POST)
            if form.is_valid():
                titulo = form.cleaned_data['titulo']
                mensaje = form.cleaned_data['mensaje']
                nuevo_mensaje = Mensaje.objects.create(
                    titulo=titulo,
                    mensaje=mensaje,
                    foro=obj_foro,
                    usuario=usuario,
                )
                return redirect("userMostrarForo")
            else:
                return HttpResponse("Error en formulario")

    # creamos un form para el mensaje
    form = FormMensaje()
    return render(response, 'userCrearMensaje.html', {'form': form, 'usuario': usuario})


def adminCrearForo(response):
    """
        Permite crear un foro.
    """
    # obtenemos al usuario
    usuario = response.user

    if response.method == "POST":
        # obtenemos boton crear
        btn_crear = response.POST.get('crear')
        if btn_crear == "Foro":
            # en caso de que tenga peticion post
            form = FormCrearForo(response.POST)
            if form.is_valid():
                nombre = form.cleaned_data['nombre']
                descripcion = form.cleaned_data['descripcion']
                nuevo_foro = Foro.objects.create(
                    nombre=nombre,
                    descripcion=descripcion,
                )
                nuevo_foro.participantes.add(usuario)

                response.session['foro'] = nombre
                return redirect("adminMostrarCodigo")

    form = FormCrearForo()
    return render(response, 'adminCrearForo.html', {'usuario': usuario, 'form': form})


def adminMostrarCodigo(response):
    """
        Muestra el codigo generado para ingresar a foro
    """
    usuario = response.user
    # obtenemos el nombre del foro
    nombre_foro = response.session.get('foro')
    # obtenemos el objeto foro
    obj_foro = Foro.objects.get(nombre=nombre_foro)

    return render(response, 'adminMostrarCodigo.html', {'usuario': usuario, 'foro': obj_foro})
