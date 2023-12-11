from django.shortcuts import render, redirect
from .models import Gasto
from .forms import GastoForm

#def home(request):
    #return render(request,'usuarios/cadastrar_gasto.html')

def cadastrar_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_gastos')  # Redirecione para a página de lista de gastos
    else:
        form = GastoForm()

    return render(request, 'gastos/cadastrar_gasto.html', {'form': form})

 

    #def gastos(request):
    # salva os dados da tela para o banco de dados
    #novo_gasto = Gasto()
    #novo_gasto.categoria = request.POST.get('categoria')
   #novo_gasto.valor = request.POST.get('valor')
    #novo_gasto.periodo = request.POST.get('data')
    #novo_gasto.save()



