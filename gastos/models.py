from django.db import models


class Gasto(models.Model):
    categoria = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    periodo = models.DateField()

    def __str__(self):
        return f"{self.categoria} - {self.valor} - {self.periodo}"
