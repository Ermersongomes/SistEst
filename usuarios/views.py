from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def view_cad_usuario(request):

    if request.POST:
        post = request.POST
        form = RegisterForm(post)
        form.save()
    else:
        form = RegisterForm()

    return render(request, 'cadusuario.html', {'form': form})