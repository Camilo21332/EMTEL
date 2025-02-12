from django import forms
from apps.Trabajadores.models import Procesador,Referencia, Windows,TipoDeDisco,MarcaDelEquipo,Procesador,Ram,ReferenciasDeLicencias,UltimosDigitosDeLicencia,LicenciadosDeOffice,MantenimientoDeEquipo,Office
from django.contrib.auth.forms import UserCreationForm
from .models import Persona
from django.contrib.auth.forms import AuthenticationForm
      
#FORMS DE REGISTRO



class PersonaLoginForm(AuthenticationForm):
    username = forms.CharField(label="Documento", widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)



from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Persona

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


    
class Form_referencia(forms.ModelForm):
    
    class Meta:
        model = Referencia
        fields = [
            'referencia'
        ]
        
class Form_office(forms.ModelForm):
    
    class Meta:
        model = Office
        fields = [
            'office'
        ]
    
class Form_windows(forms.ModelForm):
    
    class Meta:
        model = Windows
        fields = [
            'windows'
        ]
    
class Form_tipodedisco(forms.ModelForm):
    
    class Meta:
        model = TipoDeDisco
        fields = [
            'tipodedisco'
        ]
        
        
class Form_marcadelequipo(forms.ModelForm):
    
    class Meta:
        model = MarcaDelEquipo
        fields = [
            'marcadelequipo'
        ]
    

class Form_procesador(forms.ModelForm):
    
    class Meta:
        model = Procesador
        fields = [
            'procesador'
        ]
    
class Form_ram(forms.ModelForm):
    
    class Meta:
        model = Ram
        fields = [
            'ram'
        ]
    
     
class Form_referenciasdelicencias(forms.ModelForm):
    
    class Meta:
        model = ReferenciasDeLicencias
        fields = [
            'referenciasdelicencias'
        ]
    
    
class Form_ultimosdigitosdelicencia(forms.ModelForm):
    
    class Meta:
        model = UltimosDigitosDeLicencia
        fields = [
            'ultimosdigitosdelicencia'
        ]
        
class Form_licenciadosdeoffice(forms.ModelForm):
    
    class Meta:
        model = LicenciadosDeOffice
        fields = [
            'licenciadosdeoffice'
        ]
        
class Form_mantenimientodeequipo(forms.ModelForm):
    
    class Meta:
        model = MantenimientoDeEquipo
        fields = [
            'mantenimientodeequipo'
        ]
        