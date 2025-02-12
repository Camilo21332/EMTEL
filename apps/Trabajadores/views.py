from django.shortcuts import render
from apps.Trabajadores.models import Referencia,Windows,Office,TipoDeDisco,MarcaDelEquipo,Procesador,Ram,ReferenciasDeLicencias,UltimosDigitosDeLicencia,LicenciadosDeOffice,MantenimientoDeEquipo
from apps.Trabajadores.forms import Form_referencia,Form_windows,Form_office,Form_tipodedisco,Form_marcadelequipo,Form_procesador,Form_ram,Form_referenciasdelicencias,Form_ultimosdigitosdelicencia,Form_licenciadosdeoffice,Form_mantenimientodeequipo,PersonaForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView,DeleteView
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from apps.Trabajadores.forms import  LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from apps.Trabajadores.decorators import permission_required
from django.contrib.auth.models import Permission
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import PersonaForm
from .forms import PersonaLoginForm

def Home(request):
    
    return render(request, 'home.html')


#INICIO DE SESION DE PERSONA
def login_view(request):
    if request.method == "POST":
        form = PersonaLoginForm(data=request.POST)
        if form.is_valid():
            documento = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=documento, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  # Redirige a la página principal después de iniciar sesión
    else:
        form = PersonaLoginForm()
    return render(request, "login.html", {"form": form})

#REGISTRO DE PERSONA


def registro(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente
            return redirect('trabajadores:Home')  # Redirige a la página de inicio
    else:
        form = PersonaForm()
    return render(request, 'registro.html', {'form': form})





def Cierre_sesion(request):
    logout(request)
    return redirect('personas:inicio_sesion')

#CRUD MODALIDAD



    
    
    #referencias
    
def Referencia_index(request):
    view_referencia = Referencia.objects.all()
    form_referencia = Form_referencia
    
    context = {
        'view_referencia': view_referencia,
        'form_referencia': form_referencia,
    }
    
    return render(request, 'referencia.html', context)

class Referencia_create(CreateView):
    model = Referencia
    form_class = Form_referencia
    template_name = 'referencia.html'
    success_url = reverse_lazy('trabajadores:referencia_index')

class Referencia_delete(DeleteView):
    model = Referencia
    success_url = reverse_lazy('trabajadores:referencia_index')

class Referencia_edit(UpdateView):
    model = Referencia
    form_class = Form_referencia
    fields = ['referencia']
    success_url = reverse_lazy('trabajadores:referencia_index')


#windows


def Windows_index(request):
    view_windows = Windows.objects.all()
    form_windows = Form_windows
    
    context = {
        'view_windows': view_windows,
        'form_windows': form_windows,
    }
    
    return render(request, 'windows.html', context)

class Windows_create(CreateView):
    model = Windows
    form_class = Form_windows
    template_name = 'windows.html'
    success_url = reverse_lazy('trabajadores:windows_index')

class Windows_delete(DeleteView):
    model = Windows
    success_url = reverse_lazy('trabajadores:windows_index')

class Windows_edit(UpdateView):
    model = Windows
    form_class = Form_windows
    fields = ['windows']
    success_url = reverse_lazy('trabajadores:windows_index')


#office

def Office_index(request):
    view_office = Office.objects.all()
    form_office = Form_office
    
    context = {
        'view_office': view_office,
        'form_office': form_office,
    }
    
    return render(request, 'office.html', context)

class Office_create(CreateView):
    model = Office
    form_class = Form_office
    template_name = 'office.html'
    success_url = reverse_lazy('trabajadores:office_index')

class Office_delete(DeleteView):
    model = Office
    success_url = reverse_lazy('trabajadores:office_index')

class Office_edit(UpdateView):
    model = Office
    form_class = Form_office
    fields = ['office']
    success_url = reverse_lazy('trabajadores:office_index')


#tipodedisco

def TipoDeDisco_index(request):
    view_tipodedisco = TipoDeDisco.objects.all()
    form_tipodedisco = Form_tipodedisco
    
    context = {
        'view_tipodedisco': view_tipodedisco,
        'form_tipodedisco': form_tipodedisco,
    }
    
    return render(request, 'tipodedisco.html', context)

class TipoDeDisco_create(CreateView):
    model = TipoDeDisco
    form_class = Form_tipodedisco
    template_name = 'tipodedisco.html'
    success_url = reverse_lazy('trabajadores:tipodedisco_index')

class TipoDeDisco_delete(DeleteView):
    model = TipoDeDisco
    success_url = reverse_lazy('trabajadores:tipodedisco_index')

class TipoDeDisco_edit(UpdateView):
    model = TipoDeDisco
    form_class = Form_tipodedisco
    fields = ['tipodedisco']
    success_url = reverse_lazy('trabajadores:tipodedisco_index')



#marca del equipo

def MarcaDelEquipo_index(request):
    view_marcadelequipo = MarcaDelEquipo.objects.all()
    form_marcadelequipo = Form_marcadelequipo
    
    context = {
        'view_marcadelequipo': view_marcadelequipo,
        'form_marcadelequipo': form_marcadelequipo,
    }
    
    return render(request, 'marcadelequipo.html', context)

class MarcaDelEquipo_create(CreateView):
    model = MarcaDelEquipo
    form_class = Form_marcadelequipo
    template_name = 'marcadelequipo.html'
    success_url = reverse_lazy('trabajadores:marcadelequipo_index')

class MarcaDelEquipo_delete(DeleteView):
    model = MarcaDelEquipo
    success_url = reverse_lazy('trabajadores:marcadelequipo_index')

class MarcaDelEquipo_edit(UpdateView):
    model = MarcaDelEquipo
    form_class = Form_marcadelequipo
    fields = ['marcadelequipo']
    success_url = reverse_lazy('trabajadores:marcadelequipo_index')


#procesador

def Procesador_index(request):
    view_procesador = Procesador.objects.all()
    form_procesador = Form_procesador
    
    context = {
        'view_procesador': view_procesador,
        'form_procesador': form_procesador,
    }
    
    return render(request, 'procesador.html', context)

class Procesador_create(CreateView):
    model = Procesador
    form_class = Form_procesador
    template_name = 'procesador.html'
    success_url = reverse_lazy('trabajadores:procesador_index')

class Procesador_delete(DeleteView):
    model = Procesador
    success_url = reverse_lazy('trabajadores:procesador_index')

class Procesador_edit(UpdateView):
    model = Procesador
    form_class = Form_procesador
    fields = ['procesador']
    success_url = reverse_lazy('trabajadores:procesador_index')


#ram

def Ram_index(request):
    view_ram = Ram.objects.all()
    form_ram = Form_ram
    
    context = {
        'view_ram': view_ram,
        'form_ram': form_ram,
    }
    
    return render(request, 'ram.html', context)

class Ram_create(CreateView):
    model = Ram
    form_class = Form_ram
    template_name = 'ram.html'
    success_url = reverse_lazy('trabajadores:ram_index')

class Ram_delete(DeleteView):
    model = Ram
    success_url = reverse_lazy('trabajadores:ram_index')

class Ram_edit(UpdateView):
    model = Ram
    form_class = Form_ram
    fields = ['ram']
    success_url = reverse_lazy('trabajadores:ram_index')


#referencias de licencias 
def ReferenciasDeLicencias_index(request):
    view_referenciasdelicencias = ReferenciasDeLicencias.objects.all()
    form_referenciasdelicencias = Form_referenciasdelicencias
    
    context = {
        'view_referenciasdelicencias': view_referenciasdelicencias,
        'form_referenciasdelicencias': form_referenciasdelicencias,
    }
    
    return render(request, 'referenciadelicencias.html', context)

class ReferenciasDeLicencias_create(CreateView):
    model = ReferenciasDeLicencias
    form_class = Form_referenciasdelicencias
    template_name = 'referenciadelicencias.html'
    success_url = reverse_lazy('trabajadores:referenciasdelicencias_index')

class ReferenciasDeLicencias_delete(DeleteView):
    model = ReferenciasDeLicencias
    success_url = reverse_lazy('trabajadores:referenciasdelicencias_index')

class ReferenciasDeLicencias_edit(UpdateView):
    model = ReferenciasDeLicencias
    form_class = Form_referenciasdelicencias
    fields = ['referenciasdelicencias']
    success_url = reverse_lazy('trabajadores:referenciasdelicencias_index')


#UltimosDigitosDeLicencias
def UltimosDigitosDeLicencia_index(request):
    view_ultimosdigitosdelicencia = UltimosDigitosDeLicencia.objects.all()
    form_ultimosdigitosdelicencia = Form_ultimosdigitosdelicencia
    
    context = {
        'view_ultimosdigitosdelicencia': view_ultimosdigitosdelicencia,
        'form_ultimosdigitosdelicencia': form_ultimosdigitosdelicencia,
    }
    
    return render(request, 'ultimosdigitosdelicencia.html', context)

class UltimosDigitosDeLicencia_create(CreateView):
    model = UltimosDigitosDeLicencia
    form_class = Form_ultimosdigitosdelicencia
    template_name = 'ultimosdigitosdelicencia.html'
    success_url = reverse_lazy('trabajadores:ultimosdigitosdelicencia_index')

class UltimosDigitosDeLicencia_delete(DeleteView):
    model = UltimosDigitosDeLicencia
    success_url = reverse_lazy('trabajadores:ultimosdigitosdelicencia_index')

class UltimosDigitosDeLicencia_edit(UpdateView):
    model = UltimosDigitosDeLicencia
    form_class = Form_ultimosdigitosdelicencia
    fields = ['ultimosdigitosdelicencia']
    success_url = reverse_lazy('trabajadores:ultimosdigitosdelicencia_index')


#licenciadosdeoffice
def LicenciadosDeOffice_index(request):
    view_licenciadosdeoffice = LicenciadosDeOffice.objects.all()
    form_licenciadosdeoffice = Form_licenciadosdeoffice
    
    context = {
        'view_licenciadosdeoffice': view_licenciadosdeoffice,
        'form_licenciadosdeoffice': form_licenciadosdeoffice,
    }
    
    return render(request, 'licenciadosdeoffice.html', context)

class LicenciadosDeOffice_create(CreateView):
    model = LicenciadosDeOffice
    form_class = Form_licenciadosdeoffice
    template_name = 'licenciadosdeoffice.html'
    success_url = reverse_lazy('trabajadores:licenciadosdeoffice_index')

class LicenciadosDeOffice_delete(DeleteView):
    model = LicenciadosDeOffice
    success_url = reverse_lazy('trabajadores:licenciadosdeoffice_index')

class LicenciadosDeOffice_edit(UpdateView):
    model = LicenciadosDeOffice
    form_class = Form_licenciadosdeoffice
    fields = ['licenciadosdeoffice']
    success_url = reverse_lazy('trabajadores:licenciadosdeoffice_index')

#mantenimientodeequipo

def MantenimientoDeEquipo_index(request):
    view_mantenimientodeequipo = MantenimientoDeEquipo.objects.all()
    form_mantenimientodeequipo = Form_mantenimientodeequipo
    
    context = {
        'view_mantenimientodeequipo': view_mantenimientodeequipo,
        'form_mantenimientodeequipo': form_mantenimientodeequipo,
    }
    
    return render(request, 'mantenimientodeequipo.html', context)

class MantenimientoDeEquipo_create(CreateView):
    model = MantenimientoDeEquipo
    form_class = Form_mantenimientodeequipo
    template_name = 'mantenimientodeequipo.html'
    success_url = reverse_lazy('trabajadores:mantenimientodeequipo_index')

class MantenimientoDeEquipo_delete(DeleteView):
    model = MantenimientoDeEquipo
    success_url = reverse_lazy('trabajadores:mantenimientodeequipo_index')

class MantenimientoDeEquipo_edit(UpdateView):
    model = MantenimientoDeEquipo
    form_class = Form_mantenimientodeequipo
    fields = ['mantenimientodeequipo']
    success_url = reverse_lazy('trabajadores:mantenimientodeequipo_index')
