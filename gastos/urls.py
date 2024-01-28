# gastos/urls.py
from django.urls import path, include
from .views import home, listar_gastos, cadastrar_gasto, atualizar_gasto, remover_gasto, cadastrar_usuario, cadastrar_receita, login_usuario, quem_somos, guia_completo,configuracoes,home_logado,atualizar_usuario, listar_usuario, atualizar_receita, listar_receita, remover_receita, atualizar_usuario, listar_usuario, atualizar_receita, listar_receita, remover_receita
from gastos import views
from accounts.views import register

urlpatterns = [
    path('',home, name='home'),
    path('listar/', listar_gastos, name='listar_gastos'),
    path('cadastrar/', cadastrar_gasto, name='cadastrar_gasto'),
    path('gastos/<int:pk>/atualizar/', atualizar_gasto, name='atualizar_gasto'),
    path('gastos/<int:pk>/remover/', remover_gasto, name='remover_gasto'),
    path('atualizar_usuario/', atualizar_usuario, name='atualizar_usuario'),
    path('listar_usuario/', listar_usuario, name='listar_usuario'),
    path('cadastrar_receita/', cadastrar_receita, name='cadastrar_receita'),
    path('atualizar_receita/', atualizar_receita, name='atualizar_receita'),
    path('listar_receita/', listar_receita, name='listar_receita'),
    path('deletar_receita/', remover_receita, name='deletar_receita'),
    path('login/', login_usuario, name='login'),
    path('quem_somos/', quem_somos, name='quem_somos'),
    path('guia_completo/', guia_completo, name='guia_completo'),
    path('configuracoes/', configuracoes, name='configuracoes'),
    path('home_logado/', home_logado, name='home_logado'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('register/', include('accounts.urls')),
    
]
