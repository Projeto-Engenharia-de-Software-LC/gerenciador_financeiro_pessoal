# gastos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GastoForm, UsuarioForm, ReceitaForm, LoginForm, AtualizarUsuarioForm
from django.contrib.auth import authenticate, login, logout   
from .models import Gasto, Receita

def home(request):
    return render(request,'pages/home.html')


#GASTOS

def atualizar_gasto(request, pk):
    gasto = Gasto.objects.get(pk=pk)
    form = GastoForm(request.POST or None, instance=gasto)
    if form.is_valid():
        form.save()
        return redirect('listar_gastos')
    return render(request, 'pages/atualizar_gasto.html', {'form': form, 'gasto': gasto})

def remover_gasto(request, pk):
    gasto = get_object_or_404(Gasto, pk=pk)
    if request.method == 'POST':
        gasto.delete()
        return redirect('listar_gastos')
    return render(request, 'pages/confirmar_remocao.html', {'gasto': gasto})

def listar_gastos(request):
    gastos = Gasto.objects.filter(usuario=request.user.id)
    return render(request, 'pages/listar_gastos.html', {'gastos': gastos})


def cadastrar_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.usuario = request.user
            gasto.save()
            return redirect('listar_gastos')
    else:
        form = GastoForm()
    return render(request, 'pages/cadastrar_gasto.html', {'form': form})


#RECEITA

def cadastrar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            receita = form.save(commit=False)
            receita.usuario = request.user
            receita.save()
            return redirect('listar_receita')
    else:
        form = ReceitaForm()
    return render(request, 'pages/cadastrar_receita.html', {'form': form})

def atualizar_receita(request, pk):
    receita = Receita.objects.get(pk=pk)
    form = ReceitaForm(request.POST or None, instance=receita)
    if form.is_valid():
        form.save()
        return redirect('listar_receita')
    return render(request, 'pages/atualizar_receita.html', {'form': form, 'receita': receita})

def listar_receita(request):
    receitas = Receita.objects.filter(usuario=request.user.id)
    return render(request, 'pages/listar_receita.html', {'receitas': receitas})

def remover_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    if request.method == 'POST':
        receita.delete()
        return redirect('listar_receita')
    return render(request, 'pages/deletar_receita.html', {'receita': receita})



#OUTROS
def quem_somos(request):
    return render(request,'pages/quem_somos.html')

def guia_completo(request):
    return render(request,'pages/guia_completo.html')

def painel(request):
    return render(request,'pages/painel.html')

def ajuda(request):
    return render(request,'pages/ajuda.html')



#USUARIO
def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('painel')
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UsuarioForm()
    return render(request, 'pages/signup.html', {'form': form})

def sair(request):
    logout(request)
    return redirect('login')

def atualizar_usuario(request):
    if request.method == 'POST':
        form = AtualizarUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('painel')
    else:
        form = AtualizarUsuarioForm(instance=request.user)
        
    return render(request, 'pages/atualizar_usuario.html', {'form': form})

def relatorio_gastos_receitas(request):
    receitas = Receita.objects.filter(usuario=request.user.id)
    gastos = Gasto.objects.filter(usuario=request.user.id)
    
    total_receitas = 0
    total_gastos = 0
    
    for receita in receitas:
        total_receitas += receita.valor
        
    for gasto in gastos:
        total_gastos += gasto.valor
    
    diferenca = total_receitas - total_gastos

    return render(request, 'pages/relatorio.html', {'receitas':receitas,'gastos': gastos,'total_gastos': total_gastos, 'total_receitas': total_receitas, 'diferenca': diferenca})
