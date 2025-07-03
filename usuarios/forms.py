from django import forms
from usuarios.models import Usuarios

class RegsisterForm(forms.NodelFrom):
    class Meta:
        model = Usuarios
        fields = '__all__'