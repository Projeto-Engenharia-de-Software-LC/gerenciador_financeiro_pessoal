# gastos/forms.py

from django import forms
from .models import Gasto, Receita, CustomUser
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','password']

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['categoria', 'valor', 'periodo','usuario']

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['categoria', 'valor', 'periodo','usuario']


