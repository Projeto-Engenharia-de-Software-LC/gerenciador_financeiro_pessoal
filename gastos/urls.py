
from django.urls import path
from .views import cadastrar_gasto

urlpatterns = [
    path('cadastrar_gasto/', cadastrar_gasto, name='cadastrar_gasto'),
    
]
