# gastos/urls.py
from django.urls import path
from .views import home, listar_gastos, cadastrar_gasto, atualizar_gasto, remover_gasto, cadastrar_usuario, cadastrar_receita, login_usuario, quem_somos, guia_completo,painel,atualizar_usuario, atualizar_receita, listar_receita, remover_receita, atualizar_usuario, atualizar_receita, listar_receita, remover_receita, relatorio_gastos_receitas,ajuda,sair

urlpatterns = [   
    path('',home, name='home'),
    
    #Usuario
    path('me/', atualizar_usuario, name='atualizar_usuario'),
    path('login/', login_usuario, name='login'),
    path('signup/', cadastrar_usuario, name='cadastrar_usuario'),
    path('sair/', sair, name='logout'),
    path('relatorio/', relatorio_gastos_receitas, name='relatorio_gastos_receitas'),
    path('painel/', painel, name='painel'),
    
    #Receitas
    
    path('receitas/cadastrar/', cadastrar_receita, name='cadastrar_receita'),
    path('receitas/listar/', listar_receita, name='listar_receita'),
    path('receitas/<int:pk>/atualizar/', atualizar_receita, name='atualizar_receita'),
    path('receitas/<int:pk>/remover/', remover_receita, name='deletar_receita'),
    
    #Gastos
    path('gastos/listar/', listar_gastos, name='listar_gastos'),
    path('gastos/cadastrar/', cadastrar_gasto, name='cadastrar_gasto'),
    path('gastos/<int:pk>/atualizar/', atualizar_gasto, name='atualizar_gasto'),
    path('gastos/<int:pk>/remover/', remover_gasto, name='remover_gasto'),
    
    
    #outros
    path('quem_somos/', quem_somos, name='quem_somos'),
    path('guia_completo/', guia_completo, name='guia_completo'),
    path('ajuda/', ajuda, name='ajuda'),
]
