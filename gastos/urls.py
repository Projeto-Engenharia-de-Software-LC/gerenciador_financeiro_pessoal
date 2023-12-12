# gastos/urls.py
from django.urls import path
from .views import listar_gastos, cadastrar_gasto

urlpatterns = [
    path('listar/', listar_gastos, name='listar_gastos'),
    path('', cadastrar_gasto, name='cadastrar_gasto'),
]
