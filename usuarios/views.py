from django.shortcuts import render

# Create your views here.
def view_cad_usuario(request):
    return render(request, 'cadusuario.html')