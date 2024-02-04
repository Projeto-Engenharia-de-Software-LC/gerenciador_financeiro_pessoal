# gastos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GastoForm, UsuarioForm, ReceitaForm, LoginForm
from django.contrib.auth import authenticate, login  
from .models import Gasto, Usuario, Receita
from django.db.models import Sum

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

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                user.is_staff = True
                is_active=True
                return redirect('home_logado')
                
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user= form.save()
            #login_usuario(request, user)
            return redirect('login')  # Substitua 'index' pelo nome da sua página inicial
            
    else:
        form = UsuarioForm()
    return render(request, 'cadastrar_usuario.html', {'form': form})

def atualizar_usuario(request, pk):
    username = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=username)
        if form.is_valid():
            username = form.save(commit=False)
            uusername.save()
            return redirect('listar_usuario', pk=username.pk)
    else:
        form = UsuarioForm(instance=username)
    return render(request, 'atualizar_usuario.html', {'form': form})

def listar_usuario(request):
    usuario = Usuario.objects.all()
    return render(request, 'listar_usuario.html', {'usuario': usuario})

def cadastrar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = ReceitaForm()
    return render(request, 'cadastrar_receita.html', {'form': form})

def atualizar_receita(request, pk):
    receita = Receita.objects.get(pk=pk)
    form = ReceitaForm(request.POST or None, instance=receita)
    if form.is_valid():
        form.save()
        return redirect('listar_receita')
    return render(request, 'atualizar_receita.html', {'form': form, 'receita': receita})

def listar_receita(request):
    receitas = Receita.objects.all()
    return render(request, 'listar_receita.html', {'receitas': receitas})

def remover_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    if request.method == 'POST':
        receita.delete()
        return redirect('listar_receita')
    return render(request, 'deletar_receita.html', {'receita': receita})

def relatorio_gastos_receitas(request):
    receitas = Receita.objects.all()
    gastos = Gasto.objects.all()
    total_gastos = Gasto.objects.aggregate(Sum('valor'))['valor__sum'] or 0
    total_receitas = Receita.objects.aggregate(Sum('valor'))['valor__sum'] or 0
    diferenca = total_receitas - total_gastos

    return render(request, 'relatorio.html', {'receitas':receitas,'gastos': gastos,'total_gastos': total_gastos, 'total_receitas': total_receitas, 'diferenca': diferenca})

def quem_somos(request):
    return render(request,'quem_somos.html')

def guia_completo(request):
    return render(request,'guia_completo.html')

def configuracoes(request):
    return render(request,'configuracoes.html')

def home_logado(request):
    return render(request,'home_logado.html')