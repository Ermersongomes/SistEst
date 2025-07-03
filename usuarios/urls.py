from django.urls import path, include
from usuarios.views import *

urlpatterns = [
    path('cad_usuario/', view_cad_usuario, name= 'cad_usuario'),
    path('cad_carro/', view_cad_carro, name='cad_carro'),
    path('cad_estacionamento/', view_cad_estacionamento, name='cad_estacionamento'),
]