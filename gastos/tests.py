from django.test import TestCase
from django.utils import timezone
from .models import Gasto

class GastoModelTest(TestCase):
    def setUp(self):
        # Cria alguns objetos Gasto para testar
        Gasto.objects.create(categoria='Alimentação', valor=50.00, periodo=timezone.now())
        Gasto.objects.create(categoria='Transporte', valor=30.50, periodo=timezone.now())
        Gasto.objects.create(categoria='Entretenimento', valor=100.75, periodo=timezone.now())

    def test_gasto_str_method(self):
        gasto_alimentacao = Gasto.objects.get(categoria='Alimentação')
        gasto_transporte = Gasto.objects.get(categoria='Transporte')
        gasto_entretenimento = Gasto.objects.get(categoria='Entretenimento')

        self.assertEqual(str(gasto_alimentacao), 'Alimentação - 50.00 - ' + str(gasto_alimentacao.periodo))
        self.assertEqual(str(gasto_transporte), 'Transporte - 30.50 - ' + str(gasto_transporte.periodo))
        self.assertEqual(str(gasto_entretenimento), 'Entretenimento - 100.75 - ' + str(gasto_entretenimento.periodo))
