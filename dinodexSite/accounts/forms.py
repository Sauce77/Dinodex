from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.models import User
from .models import Perfil


class LoginForm(AuthenticationForm):
    """
        Se utiliza para generer el form y autenticar
        en la vista login.
    """
    username = forms.CharField(label="Nombre de usuario", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")


class RegistroForm(UserCreationForm):
    """
        Utilizado para dar de alta un
        usuario.
    """
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class PerfilForm(forms.ModelForm):
    """
        Utilizado para poder determinar el perfil de registro
        de usuario en userMenuRegistro. Los campos no pueden ser
        editados.
    """
    class Meta:
        model = Perfil
        fields = ['id_perfil', 'nombre', 'descripcion']
        labels = {
            'id_perfil': 'perfilID',
            'nombre': 'perfilNombre',
            'descripcion': 'perfilDescripcion'
        }
        widgets = {
            'id_perfil': forms.HiddenInput(),
            'nombre': forms.TextInput(attrs={'readonly': True}),
            'descripcion': forms.TextInput(attrs={'readonly': True})
        }
