from django import forms

from .models import Foro, Mensaje


class FormCrearForo(forms.ModelForm):
    """
        Se utiliza para crear un nuevo foro. 
    """
    class Meta:
        model = Foro
        fields = ['nombre', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(),
        }


class FormMensaje(forms.ModelForm):
    """
        Se utiliza para agregar un nuevo mensaje
    """
    class Meta:
        model = Mensaje
        fields = ['titulo', 'mensaje']
        widgets = {
            'mensaje': forms.Textarea(),
        }
