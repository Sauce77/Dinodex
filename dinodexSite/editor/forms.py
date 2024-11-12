from django import forms

from dinoteca.models import Dinosaurio


class FormDinosaurio(forms.ModelForm):
    """
        Se utiliza para enviar la informacion de dinosaurios
        en el editor.
    """
    class Meta:
        model = Dinosaurio
        fields = ['id_dinosaurio']
        widgets = {'id_dinosaurio': forms.HiddenInput()}
