from django.shortcuts import render
from .models import Gasto

def home(request):
    return render(request,'usuarios/cadastrar_gasto.html')

def gastos(request):
    # salva os dados da tela para o banco de dados
    novo_gasto = Gasto()
    novo_gasto.categoria = request.POST.get('categoria')
    novo_gasto.valor = request.POST.get('valor')
    novo_gasto.periodo = request.POST.get('data')
    novo_gasto.save()


