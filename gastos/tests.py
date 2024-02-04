from django.test import TestCase
from django.utils import timezone
from .models import Receita

class ReceitaModelTest(TestCase):
    def setUp(self):
        # Cria alguns objetos Gasto para testar
        Receita.objects.create(categoria='Salario', valor=2570.00, periodo=timezone.now())
        Receita.objects.create(categoria='Freelance', valor=1982.00, periodo=timezone.now())
        Receita.objects.create(categoria='Extra', valor=457.00, periodo=timezone.now())
        
    def test_receita_str_method(self):
        receita_salario = Receita.objects.get(categoria='Alimentação')
        receita_freelance = Receita.objects.get(categoria='Transporte')
        receita_extra = Receita.objects.get(categoria='Entretenimento')

        self.assertEqual(str(receita_salario), 'Salario - 2570.00 - ' + str(receita_salario.periodo))
        self.assertEqual(str(receita_freelance), 'Freelance - 1982.00 - ' + str(receita_freelance.periodo))
        self.assertEqual(str(receita_extra), 'Extra - 457.00 - ' + str(receita_extra.periodo))