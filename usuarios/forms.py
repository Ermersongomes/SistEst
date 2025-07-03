from django import forms
from usuarios.models import Usuarios

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'