# gastos/forms.py

from django import forms
from .models import Gasto, PerfilUsuario, Receita, Usuario
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'cpf', 'data_nasc','email','password']

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = '__all__'

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['categoria', 'valor', 'periodo']


