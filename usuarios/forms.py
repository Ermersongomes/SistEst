from django import forms
from usuarios.models import Usuarios, Carros, Estacionamentos

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'

class CarroForm():
    class Meta:
        model = Carros
        fields = '__all__'

class EstacionamentoForm():
    class Meta:
        model = Estacionamentos
        fields = '__all__'