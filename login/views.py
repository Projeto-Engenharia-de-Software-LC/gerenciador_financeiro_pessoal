from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from gastos.forms import LoginForm, UsuarioForm
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

# Create your views here.
def home(request):
    return render(request, 'home.html')

def home_logado(request):
    return render(request, 'base_logado.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o usuário
            login(request, user)  # Faz o login do usuário
            return redirect('home_logado')  # Redireciona para a página inicial após o cadastro
    else:
        form = UsuarioForm()
    return render(request, 'cadastrar_usuario.html', {'form': form})

def logar(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("user", request.POST.get('username'))
        print("password", request.POST.get('password'))
        User = get_user_model()
        user_exists = User.objects.filter(username=request.POST.get('username')).exists()
        print("USERS:", user_exists)
        if user_exists:
            user = form.get_user()
            login(request, user)
            return redirect('home_logado')  # Redireciona para a página inicial após o login
        else:
            print("ERRO", form.is_valid())
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})