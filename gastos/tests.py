<<<<<<< HEAD
from django.test import TestCase, RequestFactory
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Usuario, Receita, Gasto
from .forms import LoginForm, UsuarioForm, ReceitaForm, GastoForm
from gastos.views import cadastrar_usuario, home, home_logado, listar_usuario, login_usuario, quem_somos, relatorio_gastos_receitas

class GastoModelTest(TestCase):
    def setUp(self):
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

class CustomUserTest(TestCase):
    def test_custom_user_creation(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword'))

class UsuarioTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_usuario_creation(self):
        usuario = Usuario.objects.create(
            username='testuser2',
            email='test2@example.com',
            password='testpass2'
        )
        self.assertEqual(usuario.username, 'testuser2')
        self.assertEqual(usuario.email, 'test2@example.com')
        self.assertEqual(usuario.password, 'testpass2')

    def test_usuario_str_method(self):
        usuario = Usuario.objects.create(
            username='testuser2',
            email='test2@example.com',
            password='testpass2'
        )
        self.assertEqual(str(usuario), 'testuser2 - test2@example.com')

class ReceitaTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_receita_creation(self):
        usuario = Usuario.objects.create(
            username='testuser2',
            email='test2@example.com',
            password='testpass2'
        )
        receita = Receita.objects.create(
            usuario=usuario,
            categoria='Test Categoria',
            valor=100.50,
            periodo='2024-02-05'
        )
        self.assertEqual(receita.usuario, usuario)
        self.assertEqual(receita.categoria, 'Test Categoria')
        self.assertEqual(receita.valor, 100.50)
        self.assertEqual(str(receita.periodo), '2024-02-05')

class ViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_home_view(self):
        request = self.factory.get(reverse('home'))
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_login_usuario_view(self):
        request = self.factory.post(reverse('login_usuario'), data={'username': 'testuser', 'password': 'testpassword'})
        response = login_usuario(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home_logado'))

    def test_cadastrar_usuario_view(self):
        request = self.factory.post(reverse('cadastrar_usuario'), data={'username': 'newuser', 'email': 'new@example.com', 'password': 'newpassword'})
        response = cadastrar_usuario(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))

    def test_listar_usuario_view(self):
        request = self.factory.get(reverse('listar_usuario'))
        response = listar_usuario(request)
        self.assertEqual(response.status_code, 200)

    def test_relatorio_gastos_receitas_view(self):
        request = self.factory.get(reverse('relatorio_gastos_receitas'))
        response = relatorio_gastos_receitas(request)
        self.assertEqual(response.status_code, 200)

    def test_quem_somos_view(self):
        request = self.factory.get(reverse('quem_somos'))
        response = quem_somos(request)
        self.assertEqual(response.status_code, 200)

    def test_home_logado_view(self):
        request = self.factory.get(reverse('home_logado'))
        response = home_logado(request)
        self.assertEqual(response.status_code, 200)

class FormsTestCase(TestCase):
    def test_login_form_valid_data(self):
        form_data = {'username': 'testuser', 'password': 'testpassword'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid_data(self):
        form_data = {'username': 'testuser'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_valid_data(self):
        form_data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpassword'}
        form = UsuarioForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_invalid_data(self):
        form_data = {'username': 'testuser', 'email': 'invalid_email', 'password': 'testpassword'}
        form = UsuarioForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_receita_form_valid_data(self):
        usuario = Usuario.objects.create(username='testuser', email='test@example.com', password='testpassword')
        form_data = {'categoria': 'Test Categoria', 'valor': 100.50, 'periodo': '2024-02-05', 'usuario': usuario.id}
        form = ReceitaForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_receita_form_invalid_data(self):
        form_data = {'categoria': 'Test Categoria', 'valor': 'invalid_value', 'periodo': '2024-02-05', 'usuario': 'invalid_user'}
        form = ReceitaForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_gasto_form_valid_data(self):
        usuario = Usuario.objects.create(username='testuser', email='test@example.com', password='testpassword')
        form_data = {'categoria': 'Test Categoria', 'valor': 100.50, 'periodo': '2024-02-05', 'usuario': usuario.id}
        form = GastoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_gasto_form_invalid_data(self):
        form_data = {'categoria': 'Test Categoria', 'valor': 'invalid_value', 'periodo': '2024-02-05', 'usuario': 'invalid_user'}
        form = GastoForm(data=form_data)
        self.assertFalse(form.is_valid())
=======
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
>>>>>>> feature-implementacao-CRUD-de-receitas
