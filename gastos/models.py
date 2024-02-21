from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    # Adicione campos personalizados, se necessário
    pass

class Usuario(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.username} - {self.email}"

class Receita(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    periodo = models.DateField()

class Gasto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    periodo = models.DateField()

    def __str__(self):
        return f"{self.categoria} - {self.valor} - {self.periodo}"
