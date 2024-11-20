from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.models import User
from .models import Perfil


class LoginForm(AuthenticationForm):
    """
        Se utiliza para generer el form y autenticar
        en la vista login.
    """
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                               'class': 'form-control w-100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                               'class': 'form-control w-100'}))


class RegistroForm(UserCreationForm):
    """
        Utilizado para dar de alta un
        usuario.
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': ' form-control', 'placeholder': 'Apellido'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}),
            'username': forms.TextInput(attrs={'class': ' form-control', 'placeholder': 'Usuario'}),
        }


class PerfilForm(forms.ModelForm):
    """
        Utilizado para poder determinar el perfil de registro
        de usuario en userMenuRegistro. Los campos no pueden ser
        editados.
    """
    class Meta:
        model = Perfil
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'readonly': True, 'class': 'text-center bg-transparent profile-option'}),
            'descripcion': forms.HiddenInput(attrs={'readonly': True, 'class': ' formPerfil'})
        }
