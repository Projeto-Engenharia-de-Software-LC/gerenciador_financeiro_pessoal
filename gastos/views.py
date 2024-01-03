# gastos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GastoForm, UsuarioForm, ReceitaForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import Gasto, PerfilUsuario, Receita

def home(request):
    return render(request,'home.html')

def atualizar_gasto(request, pk):
    gasto = Gasto.objects.get(pk=pk)
    form = GastoForm(request.POST or None, instance=gasto)
    if form.is_valid():
        form.save()
        return redirect('listar_gastos')
    return render(request, 'atualizar_gasto.html', {'form': form, 'gasto': gasto})

def remover_gasto(request, pk):
    gasto = get_object_or_404(Gasto, pk=pk)
    if request.method == 'POST':
        gasto.delete()
        return redirect('listar_gastos')
    return render(request, 'confirmar_remocao.html', {'gasto': gasto})

def listar_gastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'listar_gastos.html', {'gastos': gastos})


def cadastrar_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_gastos')
    else:
        form = GastoForm()
    return render(request, 'cadastrar_gasto.html', {'form': form})

    def login(request):
        if request.method == 'POST':
            form = LoginForm(request, request.POST)
            if form.is_valid():
                user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('home.html')  
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect('home.html')  # Substitua 'index' pelo nome da sua página inicial
    else:
        form = UsuarioForm()
    return render(request, 'cadastrar_usuario.html', {'form': form})

def cadastrar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.html')  # Substitua 'index' pelo nome da sua página inicial
    else:
        form = ReceitaForm()
    return render(request, 'cadastrar_receita.html', {'form': form})


def quem_somos(request):
    return render(request,'quem_somos.html')

def guia_completo(request):
    return render(request,'guia_completo.html')

def configuracoes(request):
    return render(request,'configuracoes.html')