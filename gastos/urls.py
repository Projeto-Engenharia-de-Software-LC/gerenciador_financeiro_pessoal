# gastos/urls.py
from django.urls import path
from .views import home, listar_gastos, cadastrar_gasto, atualizar_gasto, remover_gasto

urlpatterns = [
    path('',home, name='home'),
    path('listar/', listar_gastos, name='listar_gastos'),
    path('cadastrar/', cadastrar_gasto, name='cadastrar_gasto'),
    path('gastos/<int:pk>/atualizar/', atualizar_gasto, name='atualizar_gasto'),
    path('gastos/<int:pk>/remover/', remover_gasto, name='remover_gasto'),
]
