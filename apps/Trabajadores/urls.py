from django.urls import path
from apps.Trabajadores import views as core_views


app_name = 'trabajadores'
urlpatterns = [
    
    path('home/', core_views.Home, name='Home'),
    path('cierre_sesion/', core_views.Cierre_sesion, name='cierre_sesion'),
    path('inicio_sesion/', core_views.login_view, name='inicio_sesion'),
    path('registro/', core_views.registro, name='registro'),


    
    path('referencia/index/', core_views.Referencia_index, name='referencia_index'),
    path('referencia/create/', core_views.Referencia_create.as_view(), name='referencia_create'),
    path('referencia/delete/<int:pk>', core_views.Referencia_delete.as_view(), name='referencia_delete'),
    path('referencia/edit/<int:pk>', core_views.Referencia_edit.as_view(), name='referencia_edit'),
    
    
    
    path('windows/index/', core_views.Windows_index, name='windows_index'),
    path('windows/create/', core_views.Windows_create.as_view(), name='Windows_create'),
    path('windows/delete/<int:pk>', core_views.Windows_delete.as_view(), name='windows_delete'),
    path('windows/edit/<int:pk>', core_views.Windows_edit.as_view(), name='windows_edit'),
    
    
    path('office/index/', core_views.Office_index, name='office_index'),
    path('office/create/', core_views.Office_create.as_view(), name='office_create'),
    path('office/delete/<int:pk>', core_views.Office_delete.as_view(), name='office_delete'),
    path('office/edit/<int:pk>', core_views.Office_edit.as_view(), name='office_edit'),
    
    
    
    path('tipo-de-disco/index/', core_views.TipoDeDisco_index, name='tipo_de_disco_index'),
    path('tipo-de-disco/create/', core_views.TipoDeDisco_create.as_view(), name='tipo_de_disco_create'),
    path('tipo-de-disco/delete/<int:pk>', core_views.TipoDeDisco_delete.as_view(), name='tipo_de_disco_delete'),
    path('tipo-de-disco/edit/<int:pk>', core_views.TipoDeDisco_edit.as_view(), name='tipo_de_disco_edit'),
    
    
    path('marca-del-equipo/index/', core_views.MarcaDelEquipo_index, name='marca_del_equipo_index'),
    path('marca-del-equipo/create/', core_views.MarcaDelEquipo_create.as_view(), name='marca_del_equipo_create'),
    path('marca-del-equipo/delete/<int:pk>', core_views.MarcaDelEquipo_delete.as_view(), name='marca_del_equipo_delete'),
    path('marca-del-equipo/edit/<int:pk>', core_views.MarcaDelEquipo_edit.as_view(), name='marca_del_equipo_edit'),
    
    
    path('procesador/index/', core_views.Procesador_index, name='procesador_index'),
    path('procesador/create/', core_views.Procesador_create.as_view(), name='procesador_create'),
    path('procesador/delete/<int:pk>', core_views.Procesador_delete.as_view(), name='procesador_delete'),
    path('procesador/edit/<int:pk>', core_views.Procesador_edit.as_view(), name='procesador_edit'),
    
    
    path('ram/index/', core_views.Ram_index, name='ram_index'),
    path('ram/create/', core_views.Ram_create.as_view(), name='ram_create'),
    path('ram/delete/<int:pk>', core_views.Ram_delete.as_view(), name='ram_delete'),
    path('ram/edit/<int:pk>', core_views.Ram_edit.as_view(), name='ram_edit'),
    
    path('referencias-de-licencias/index/', core_views.ReferenciasDeLicencias_index, name='referencias_de_licencias_index'),
    path('referencias-de-licencias/create/', core_views.ReferenciasDeLicencias_create.as_view(), name='referencias_de_licencias_create'),
    path('referencias-de-licencias/delete/<int:pk>', core_views.ReferenciasDeLicencias_delete.as_view(), name='referencias_de_licencias_delete'),
    path('referencias-de-licencias/edit/<int:pk>', core_views.ReferenciasDeLicencias_edit.as_view(), name='referencias_de_licencias_edit'),
    
    
    path('ultimos-digitos-de-licencia/index/', core_views.UltimosDigitosDeLicencia_index, name='ultimos_digitos_de_licencia_index'),
    path('ultimos-digitos-de-licencia/create/', core_views.UltimosDigitosDeLicencia_create.as_view(), name='ultimos_digitos_de_licencia_create'),
    path('ultimos-digitos-de-licencia/delete/<int:pk>', core_views.UltimosDigitosDeLicencia_delete.as_view(), name='ultimos_digitos_de_licencia_delete'),
    path('ultimos-digitos-de-licencia/edit/<int:pk>', core_views.UltimosDigitosDeLicencia_edit.as_view(), name='ultimos_digitos_de_licencia_edit'),
    
    path('licenciados-de-office/index/', core_views.LicenciadosDeOffice_index, name='licenciados_de_office_index'),
    path('licenciados-de-office/create/', core_views.LicenciadosDeOffice_create.as_view(), name='licenciados_de_office_create'),
    path('licenciados-de-office/delete/<int:pk>', core_views.LicenciadosDeOffice_delete.as_view(), name='licenciados_de_office_delete'),
    path('licenciados-de-office/edit/<int:pk>', core_views.LicenciadosDeOffice_edit.as_view(), name='licenciados_de_office_edit'),
    
    
    path('mantenimiento-de-equipo/index/', core_views.MantenimientoDeEquipo_index, name='mantenimiento_de_equipo_index'),
    path('mantenimiento-de-equipo/create/', core_views.MantenimientoDeEquipo_create.as_view(), name='mantenimiento_de_equipo_create'),
    path('mantenimiento-de-equipo/delete/<int:pk>', core_views.MantenimientoDeEquipo_delete.as_view(), name='mantenimiento_de_equipo_delete'),
    path('mantenimiento-de-equipo/edit/<int:pk>', core_views.MantenimientoDeEquipo_edit.as_view(), name='mantenimiento_de_equipo_edit'),
    

]