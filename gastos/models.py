from django.db import models
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class Usuario(models.Model):
    username = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=8)


class Receita(models.Model):
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    periodo = models.DateField()

class Gasto(models.Model):
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    periodo = models.DateField()

    def __str__(self):
        return f"{self.categoria} - {self.valor} - {self.periodo}"
