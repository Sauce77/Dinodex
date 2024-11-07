from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    """
        Se utiliza para generer el form y autenticar
        en la vista login.
    """
    fields = ['username', 'password']


class RegistroForm(UserCreationForm):
    """
        Utilizado para dar de alta un 
        usuario.
    """
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
