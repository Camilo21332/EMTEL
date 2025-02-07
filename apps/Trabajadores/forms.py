from django import forms
from apps.Trabajadores.models import Personas
class Form_personas(forms.ModelForm):
    
    class Meta:
        model = Personas
        fields = [
            'personas'
        ]
    