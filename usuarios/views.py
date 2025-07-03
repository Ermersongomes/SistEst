from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def view_cad_usuario(request):
    form = RegisterForm()

    return render(request, 'cadusuario.html', {'form': form})