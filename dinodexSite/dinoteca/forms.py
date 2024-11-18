from django import forms

from dinoteca.models import Dinosaurio


class FormMostrarCatalogo(forms.ModelForm):
    """
        Se utilzia para obtener el nombre del
        dinosaurio.
    """
    class Meta:
        model = Dinosaurio
        fields = ['nombre']
