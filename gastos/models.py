from django.db import models
from django.contrib.auth.models import User

class Receita(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    periodo = models.DateField()

class Gasto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    periodo = models.DateField()

    def __str__(self):
        return f"{self.categoria} - {self.valor} - {self.periodo}"
