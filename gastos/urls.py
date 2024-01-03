# gastos/urls.py
from django.urls import path
from .views import home, listar_gastos, cadastrar_gasto, atualizar_gasto, remover_gasto, cadastrar_usuario, cadastrar_receita, login, quem_somos, guia_completo,configuracoes
from gastos import views

urlpatterns = [
    path('',home, name='home'),
    path('listar/', listar_gastos, name='listar_gastos'),
    path('cadastrar/', cadastrar_gasto, name='cadastrar_gasto'),
    path('gastos/<int:pk>/atualizar/', atualizar_gasto, name='atualizar_gasto'),
    path('gastos/<int:pk>/remover/', remover_gasto, name='remover_gasto'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastrar_receita/', cadastrar_receita, name='cadastrar_receita'),
    path('login/', login, name='login'),
    path('quem_somos/', quem_somos, name='quem_somos'),
    path('guia_completo/', guia_completo, name='guia_completo'),
    path('configuracoes/', configuracoes, name='configuracoes')
    
]
