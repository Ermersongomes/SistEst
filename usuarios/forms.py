from django import forms
from usuarios.models import Usuarios, Carros, Estacionamentos

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
        #fields = ['nome', 'cpf', 'email']
        labels = {
            'nome': 'Nome Completo',
            'cpf': 'CPF',
            'num_CNH': 'Número da CNH',
            'validade_CNH': 'Validade da CNH',
            'email': 'E-mail'
        }  
        help_text = {
            'nome': 'digite o seu nome comleto',
            'email': 'Digite o seu e-mail'
        }
        error_messsages = {
            'nome' : {
                'required': 'Este campo não pode ser vazio'
            },
            'email': {
                'required': 'E-mail inválido'
            }
        }
class CarroForm(forms.ModelForm):
    class Meta:
        model = Carros
        fields = '__all__'

class EstacionamentoForm(forms.ModelForm):
    class Meta:
        model = Estacionamentos
        fields = '__all__'
        

       