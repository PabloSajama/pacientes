from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.lista_paciente, name='lista_paciente'),
    path('paciente/', views.detalle_paciente, name='detalle_paciente'),
    path('nuevo/', views.nuevo_paciente, name='nuevo_paciente'),
    path('editar/', views.editar_paciente, name='editar_paciente'),
    path('eliminar/', views.eliminar_paciente, name='eliminar_paciente'),
]