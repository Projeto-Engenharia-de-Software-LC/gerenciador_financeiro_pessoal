# gastos/forms.py

from django import forms
from .models import Gasto, Receita, Usuario
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']
        
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control'})

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','email','password']
        
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['categoria', 'valor', 'periodo','usuario']

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['categoria', 'valor', 'periodo','usuario']


