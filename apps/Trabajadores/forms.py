from django import forms
from apps.Trabajadores.models import Persona
from django.contrib.auth.forms import UserCreationForm
from .models import Persona
from django.contrib.auth.forms import AuthenticationForm
from .models import VersionWindows, VersionOffice, Disco, Procesador, Estado
from .models import Registros, VersionWindows, VersionOffice, Disco, Procesador, Estado

#FORMS DE REGISTRO



class PersonaLoginForm(AuthenticationForm):
    username = forms.CharField(label="Documento", widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)





class PersonaForm(UserCreationForm):
    class Meta:
        model = Persona
        fields = ['per_documento', 'per_nombre', 'password1', 'password2']
        labels = {
            'per_documento': 'Documento de Identidad',
            'per_nombre': 'Nombres',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Aplicar clases y placeholders a los campos
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        
        self.fields['per_documento'].widget.attrs['placeholder'] = 'Ingrese su documento'
        self.fields['per_nombre'].widget.attrs['placeholder'] = 'Ingrese sus nombres'
        self.fields['password1'].widget.attrs['placeholder'] = 'Ingrese su contraseña'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme su contraseña'

#FORMS DE INICIO DE SESION
class LoginForm(forms.Form):
    per_documento = forms.IntegerField(label='Documento de identidad')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    
    def clean_per_documento(self):
        per_documento = self.cleaned_data['per_documento']
        if not isinstance(per_documento, int):
            raise forms.ValidationError("Debe ser un número entero.")
        return per_documento

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if len(password1) < 8 or not any(char.isdigit() for char in password1) or not any(char.isalpha() for char in password1):
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres y contener números y letras.")
        return password1


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registros
        fields = '__all__'  # Incluir todos los campos

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        # Validaciones personalizadas
        self.fields['ultimos_digitos_licencia'].widget.attrs.update({'maxlength': '3'})

        # Reemplazar select vacíos por opciones disponibles
        self.fields['version_de_windows'].queryset = VersionWindows.objects.all()
        self.fields['version_de_office'].queryset = VersionOffice.objects.all()
        self.fields['disco'].queryset = Disco.objects.all()
        self.fields['procesador'].queryset = Procesador.objects.all()
        self.fields['estado'].queryset = Estado.objects.all()




#FORMS


class VersionWindowsForm(forms.ModelForm):
    class Meta:
        model = VersionWindows
        fields = ["nombre"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre de la versión de Windows"}),
        }

class VersionOfficeForm(forms.ModelForm):
    class Meta:
        model = VersionOffice
        fields = ["nombre"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre de la versión de Office"}),
        }

class DiscoForm(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ["tipo"]
        widgets = {
            "tipo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Tipo de disco"}),
        }

class ProcesadorForm(forms.ModelForm):
    class Meta:
        model = Procesador
        fields = ["nombre"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del procesador"}),
        }

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ["estado"]
        widgets = {
            "estado": forms.TextInput(attrs={"class": "form-control", "placeholder": "Estado del equipo"}),
        }
