# gastos/forms.py

from django import forms
from .models import Gasto, Receita, Usuario
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','email','password']

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['categoria', 'valor', 'periodo','usuario']

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['categoria', 'valor', 'periodo','usuario']


