from django.shortcuts import render
from apps.Trabajadores.models import Personas
from apps.Trabajadores.forms import Form_personas
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView,DeleteView
#CRUD MODALIDAD

def Personas_index(request):
    view_personas = Personas.objects.all()
    form_personas = Form_personas
    
    context = {
         'view_personas':view_personas,
         'form_personas':form_personas,
    }
    
    return render(request, 'personas.html',context)
class Personas_create(CreateView):
    model =  Personas
    form_class = Form_personas
    template_name = 'personas.html'
    success_url = reverse_lazy('trabajadores:personas_index')

class Personas_delete(DeleteView):
    print('holala pepep')
    model = Personas
    success_url = reverse_lazy('trabajadores:personas_index')

class Personas_edit(UpdateView):
    model = Personas
    from_class = Form_personas
    fields = ['personas']
    success_url = reverse_lazy('trabajadores:personas_index')
    