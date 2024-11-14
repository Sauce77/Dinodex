from django import forms

from dinoteca.models import Dinosaurio


class FormEditarCatalogo(forms.ModelForm):
    """
        Se utilzia para obtener el nombre del
        dinosaurio.
    """
    class Meta:
        model = Dinosaurio
        fields = ['nombre']


class FormEditarDinosaurio(forms.ModelForm):
    """
        Utilizado para modificar los campos de un dinosaurio
        desde la vista editorEditaDino.
    """
    class Meta:
        model = Dinosaurio
        fields = "__all__"
