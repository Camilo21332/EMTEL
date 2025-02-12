from django.urls import path
from apps.Trabajadores import views as core_views 


app_name = 'trabajadores'
urlpatterns = [
    
    path('home/', core_views.Home, name='Home'),
    path('cierre_sesion/', core_views.Cierre_sesion, name='cierre_sesion'),
    path('inicio_sesion/', core_views.login_view, name='inicio_sesion'),
    path('registro/', core_views.registro, name='registro'),



    path('lista/', core_views.lista_registros, name='lista_registros'),
    path('guardar/', core_views.guardar_registro, name='guardar_registro'),
    path('editar/<int:pk>/', core_views.editar_registro, name='editar_registro'),
    path('eliminar/<int:pk>/', core_views.eliminar_registro, name='eliminar_registro'),
    
   
    # ================= CRUD para VersionWindows =================
    path('versionwindows/', core_views.VersionWindowsListView, name='versionwindows_list'),
    path('versionwindows/create/', core_views.VersionWindowsCreateView.as_view(), name='versionwindows_create'),
    path('versionwindows/delete/<int:pk>/', core_views.VersionWindowsDeleteView.as_view(), name='versionwindows_delete'),
    path('versionwindows/update/<int:pk>/', core_views.VersionWindowsUpdateView.as_view(), name='versionwindows_update'),
    

    # Disco

    path("disco/", core_views.DiscoListView, name="disco_list"),
    path("disco/create/", core_views.DiscoCreateView.as_view(), name="disco_create"),
    path("disco/update/<int:pk>/", core_views.DiscoUpdateView.as_view(), name="disco_update"),
    path('disco/delete/<int:pk>/', core_views.DiscoDeleteView.as_view(), name='disco_delete'),




    path('version_office/', core_views.VersionOfficeListView, name='version_office_list'),
    path('version_office/create/', core_views.VersionOfficeCreateView.as_view(), name='version_office_create'),
    path('version_office/update/<int:pk>/', core_views.VersionOfficeUpdateView.as_view(), name='version_office_update'),
    path('version_office/delete/<int:pk>/', core_views.VersionOfficeDeleteView.as_view(), name='version_office_delete'),


    path('procesador/', core_views.ProcesadorListView, name='procesador_list'),
    path('procesador/create/', core_views.ProcesadorCreateView.as_view(), name='procesador_create'),
    path('procesador/update/<int:pk>/', core_views.ProcesadorUpdateView.as_view(), name='procesador_update'),
    path('procesador/delete/<int:pk>/', core_views.ProcesadorDeleteView.as_view(), name='procesador_delete'),



    path('estado/', core_views.EstadoListView, name='estado_list'),
    path('estado/create/', core_views.EstadoCreateView.as_view(), name='estado_create'),
    path('estado/update/<int:pk>/', core_views.EstadoUpdateView.as_view(), name='estado_update'),
    path('estado/delete/<int:pk>/', core_views.EstadoDeleteView.as_view(), name='estado_delete'),



]