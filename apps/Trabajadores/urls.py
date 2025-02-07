from django.urls import path
from apps.Trabajadores import views as core_views


app_name = 'trabajadores'
urlpatterns = [
     #MODALIDAD
    path('personas/index/', core_views.Personas_index, name='personas_index'),
    path('personas/create/', core_views.Personas_create.as_view(), name='personas_create'),
    path('personas/delete/<int:pk>', core_views.Personas_delete.as_view(), name='personas_delete'),
    path('personas/edit/<int:pk>', core_views.Personas_edit.as_view(), name='personas_edit'),
]