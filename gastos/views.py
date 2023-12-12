# gastos/views.py
from django.shortcuts import render, redirect
from .forms import GastoForm
from .models import Gasto


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
