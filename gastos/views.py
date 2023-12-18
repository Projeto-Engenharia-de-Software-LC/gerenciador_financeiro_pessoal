# gastos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GastoForm
from .models import Gasto

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
