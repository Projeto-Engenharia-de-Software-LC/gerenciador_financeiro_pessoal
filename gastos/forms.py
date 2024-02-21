# gastos/forms.py

from django import forms
from .models import Gasto, Receita
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control'})

class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1']
        
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password1'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        
        del self.fields['password2']
        
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None
        

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['categoria', 'valor', 'periodo','usuario']

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['categoria', 'valor', 'periodo','usuario']
