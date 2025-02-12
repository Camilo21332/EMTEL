from django.shortcuts import render
from apps.Trabajadores.models import Persona
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import PersonaForm
from .forms import PersonaLoginForm
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Registros
from .forms import RegistroForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import VersionWindows, VersionOffice, Disco, Procesador, Estado
from .forms import VersionWindowsForm, VersionOfficeForm, DiscoForm, ProcesadorForm, EstadoForm

from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
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
                return redirect("trabajadores:lista_registros")  # Redirige a la página principal después de iniciar sesión
    else:
        form = PersonaLoginForm()
    return render(request, "inicio_sesion.html", {"form": form})

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
    return redirect('trabajadores:inicio_sesion')




def lista_registros(request):
    registros = Registros.objects.all()
    form = RegistroForm()
    return render(request, 'lista.html', {'registros': registros, 'form': form})

def guardar_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            registro = form.save()
            return JsonResponse({'success': True, 'nombre': registro.nombre_apellidos})
    return JsonResponse({'success': False, 'errors': form.errors})

def editar_registro(request, pk):
    registro = get_object_or_404(Registros, pk=pk)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False})

def eliminar_registro(request, pk):
    registro = get_object_or_404(Registros, pk=pk)
    if request.method == 'POST':
        registro.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})



#CRUDS



# ================= CRUD para Disco =================


def DiscoListView(request):
    view_discos = Disco.objects.all()
    form_disco =    DiscoForm
    
    context = {
         'view_discos':view_discos,
         'form_disco':form_disco,
    }
    
    return render(request, 'disco_list.html',context)
class DiscoCreateView(CreateView):
    model =  Disco
    form_class = DiscoForm
    template_name = 'disco_index.html'
    success_url = reverse_lazy('trabajadores:disco_list')

class DiscoDeleteView(DeleteView):
    model = Disco
    success_url = reverse_lazy('trabajadores:disco_list')

class DiscoUpdateView(UpdateView):
    model = Disco
    from_class = DiscoForm
    fields = ['tipo']
    success_url = reverse_lazy('trabajadores:disco_list')
    
# ================= CRUD para VersionWindows =================

def VersionWindowsListView(request):
    view_versions = VersionWindows.objects.all()
    form_version = VersionWindowsForm
    
    context = {
         'view_versions': view_versions,
         'form_version': form_version,
    }
    
    return render(request, 'versionwindows_list.html', context)

class VersionWindowsCreateView(CreateView):
    model = VersionWindows
    from_class = VersionWindowsForm
    template_name = 'versionwindows_index.html'
    success_url = reverse_lazy('trabajadores:versionwindows_list')

class VersionWindowsDeleteView(DeleteView):
    model = VersionWindows
    success_url = reverse_lazy('trabajadores:versionwindows_list')

class VersionWindowsUpdateView(UpdateView):
    model = VersionWindows
    from_class = VersionWindowsForm  
    fields = ['nombre']
    success_url = reverse_lazy('trabajadores:versionwindows_list')


# ================= CRUD para Version Office =================

def VersionOfficeListView(request):
    view_versions = VersionOffice.objects.all()
    form_version = VersionOfficeForm
    
    context = {
         'view_versions': view_versions,
         'form_version': form_version,
    }
    
    return render(request, 'versionoffice_list.html', context)

class VersionOfficeCreateView(CreateView):
    model = VersionOffice
    form_class = VersionOfficeForm
    template_name = 'versionoffice_list.html'
    success_url = reverse_lazy('trabajadores:version_office_list')

class VersionOfficeDeleteView(DeleteView):
    model = VersionOffice
    success_url = reverse_lazy('trabajadores:version_office_list')

class VersionOfficeUpdateView(UpdateView):
    model = VersionOffice
    from_class = VersionOfficeForm  
    fields = ['nombre']
    success_url = reverse_lazy('trabajadores:version_office_list')


# ================= CRUD para Procesador =================

def ProcesadorListView(request):
    view_versions = Procesador.objects.all()
    form_version = ProcesadorForm
    
    context = {
         'view_versions': view_versions,
         'form_version': form_version,
    }
    
    return render(request, 'procesador_list.html', context)

class ProcesadorCreateView(CreateView):
    model = Procesador
    form_class = ProcesadorForm
    template_name = 'procesador_list.html'
    success_url = reverse_lazy('trabajadores:procesador_list')

class ProcesadorDeleteView(DeleteView):
    model = Procesador
    success_url = reverse_lazy('trabajadores:procesador_list')

class ProcesadorUpdateView(UpdateView):
    model = Procesador
    from_class = ProcesadorForm  
    fields = ['nombre']
    success_url = reverse_lazy('trabajadores:procesador_list')


# ================= CRUD para Estado =================

def EstadoListView(request):
    view_estados = Estado.objects.all()
    form_estado = EstadoForm
    
    context = {
         'view_estados': view_estados,
         'form_estado': form_estado,
    }
    
    return render(request, 'estado_list.html', context)

class EstadoCreateView(CreateView):
    model = Estado
    form_class = EstadoForm
    template_name = 'estado_index.html'
    success_url = reverse_lazy('trabajadores:estado_list')

class EstadoDeleteView(DeleteView):
    model = Estado
    success_url = reverse_lazy('trabajadores:estado_list')

class EstadoUpdateView(UpdateView):
    model = Estado
    from_class = EstadoForm  
    fields = ['estado']
    success_url = reverse_lazy('trabajadores:estado_list')
