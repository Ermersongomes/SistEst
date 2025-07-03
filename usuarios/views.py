from django.shortcuts import render
from .forms import RegisterForm, CarroForm, EstacionamentoForm

# Create your views here.

def view_cad_usuario(request):

    if request.POST:
        post = request.POST
        form = RegisterForm(post)
        form.save()
    else:
        form = RegisterForm()

    return render(request, 'cadusuario.html', {'form': form})

def view_cad_carro(request): 
    if request.method == 'POST':
        form = CarroForm(request.POST)
        form = RegisterForm(post)
        form.save()
            
    else:
        form = CarroForm()

    return render(request, 'cadcarro.html', {'form': form})


def view_cad_estacionamento(request):
    if request.method == 'POST':
        form = EstacionamentoForm(request.POST) # Nome do form corrigido
        form = RegisterForm(post)
        form.save()
        
    else:
        form = EstacionamentoForm() # Nome do form corrigido

    return render(request, 'cadestacionamento.html', {'form': form})