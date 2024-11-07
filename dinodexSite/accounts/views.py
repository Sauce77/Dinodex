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
    return render(request, 'example.html', {'usuario': request.user})


def userRegistro(request):
    """
        Da de alta un usuario dentro de la base de datos.
    """
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
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
                return redirect('userSuccess')
    else:
        form = LoginForm()
    return render(request, 'userLogin.html', {'form': form})


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
    # obtenemos los perfiles visibles de la base de datos
    obj_perfil_visible = Perfil.objects.filter(visible=True)
    # variable para guardar los forms de perfiles visibles
    list_forms = []

    # para cada perfil en perfiles visibles
    for obj_perfil in obj_perfil_visible:
        # creamos un formulario con el valor inicial del perfil
        formulario = PerfilForm(initial={'nombre': obj_perfil.nombre})
        list_forms.append(formulario)

    return render(request, 'userMenuPerfiles.html', {'forms': list_forms})
