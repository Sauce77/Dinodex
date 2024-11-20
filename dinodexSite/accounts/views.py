from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .forms import LoginForm, RegistroForm, PerfilForm

from .models import Perfil
# Create your views here.


@login_required
def userSuccess(request):
    """
        Solo prueba.
    """
    usuario = request.user
    obj_perfiles = Perfil.usuarios.filter(usuario=usuario)
    return render(request, 'example.html', {'usuario': request.user, 'perfiles': obj_perfiles})


def userRegistro(request):
    """
        Da de alta un usuario dentro de la base de datos.
    """
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # Recupera los datos de la sesión usando la clave "form_data"
            # Si no está presente, devolverá un diccionario vacío
            form_perfil = request.session.get("form_perfil", {})

            print(form_perfil['nombre'])
            # obtenemos el  perfil elegido
            obj_perfil = Perfil.objects.get(nombre=form_perfil['nombre'])
            # asignamos el perfil al usuario registrado
            obj_perfil.usuario.add(user)

            # Opcional: Limpia los datos después de usarlos si no los necesitas más
            # Elimina "form_data" de la sesión
            request.session.pop("form_perfil", None)
            return redirect('userLogin')
    else:
        form = RegistroForm()
    return render(request, 'userRegistro.html', {'form': form})


def userLogin(request):
    """
        Utilizado para autenticar y generar 
        la sesion del usuario.
    """
    if request.method == 'POST':
        # obtener boton login
        btn_iniciar = request.POST.get('iniciar')
        # obtener boton registrar
        btn_registarse = request.POST.get('registrar')

        if btn_iniciar == "Iniciar":
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                # Obtener los datos del formulario
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                # Autenticar al usuario
                user = authenticate(username=username, password=password)

                # si se encuentra al usuario
                if user is not None:
                    # iniciar sesion con el usaurio
                    login(request, user)
                    return redirect('userCatalogo')
        if btn_registarse == 'Registrar':
            # se pulso registar
            # agregamos los campo en la sesion
            request.session["form_perfil"] = request.POST.dict()
            return redirect('userRegistro')
    else:
        form = LoginForm()
        perfiles = Perfil.objects.filter(visible=True)

        # guardamos los forms para cada perfil
        form_perfiles = []
        for obj_perfil in perfiles:
            # para cada perfil visible
            # usamos un model form con la info del objeto
            formulario = PerfilForm(instance=obj_perfil)
            # agregamos el form a la lista
            form_perfiles.append(formulario)
        return render(request, 'userLogin.html', {'form': form, 'perfiles': form_perfiles})


def userLogout(request):
    """
        Termina la sesion del usuario activo.
    """
    logout(request)
    return redirect('userLogin')


def userMenuPerfiles(request):
    """
        Utilizado para mostrar los perfiles visibles
        para registrarse.
    """
    # se recibe una peticion POST
    if request.method == 'POST':
        # agregamos los campo en la sesion
        request.session["form_perfil"] = request.POST.dict()
        return redirect('userRegistro')

    # --------------------------------------------------------------
    # En caso de no contar con POST, renderizar los forms de perfil
    # --------------------------------------------------------------

    # obtenemos los perfiles visibles de la base de datos
    obj_perfil_visible = Perfil.objects.filter(visible=True)
    # variable para guardar los forms de perfiles visibles
    perfiles = []
    # para cada perfil en perfiles visibles
    for obj_perfil in obj_perfil_visible:
        # creamos un formulario con el valor inicial del perfil
        formulario = PerfilForm(instance=obj_perfil)
        # agregamos el form al diccionario de formularios
        perfiles.append({'form': formulario, 'imagen': obj_perfil.imagen})

    return render(request, 'userMenuPerfiles.html', {'perfiles': perfiles})
