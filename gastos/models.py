from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Usuario(models.Model):
 
    last_login = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username
    
    

class CustomUser(AbstractUser):
    telefone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username}"

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
