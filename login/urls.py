from django.urls import path
from .views import logar, cadastrar_usuario, home, home_logado

urlpatterns = [
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('login/', logar, name='login'),
    path('home/', home, name='home'),  # Adicione esta linha para a página inicial
    path('home_logado', home_logado, 'base_logado')
    # outras URLs, se necessário
]
