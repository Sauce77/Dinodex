from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.models import User


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
