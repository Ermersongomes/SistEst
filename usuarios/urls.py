from django.urls import path, include
from usuarios.views import *

urlpatterns = [
    path('cad_usuario/', view_cad_usuario),
]