# Gerenciador Financeiro Pessoal

Projeto Django para gerenciador financeiro pessoal.

Projeto em produção: https://gfp-ufrpe.rj.r.appspot.com

## Configuração do Ambiente de Desenvolvimento

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Projeto-Engenharia-de-Software-LC/gerenciador_financeiro_pessoal.git
   cd projeto-gfp
   
2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt

4. **Adicionar env no projeto:**
   1. Duplique o arquivo `.env.example`
   2. Renomeie para `.env`
   3. Adicione as informações necessárias no `.env`


5. **Aplique as migrações:**

   ```bash
   python manage.py migrate

6. **Execute o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver

## Estrutura atual do projeto

1. **Estrutura atual:**
   ```bash
   projeto_gfp/
   |-- gastos/
   |   |-- __init__.py
   |   |-- admin.py
   |   |-- apps.py
   |   |-- migrations/
   |   |   |-- __init__.py
   |   |-- models.py
   |   |-- templates/
   |   |   |-- gastos/
   |   |       |-- atualizar_gasto.html
   |   |       |-- cadastrar_gasto.html
   |   |       |-- confirmar_remocao.html
   |   |       |-- home.html
   |   |       |-- listar_gastos.html
   |   |-- tests.py
   |   |-- views.py
   |-- projeto_gastos/
   |   |-- __init__.py
   |   |-- asgi.py
   |   |-- settings.py
   |   |-- urls.py
   |   |-- wsgi.py
   |-- .gitignore
   |-- manage.py
   |-- requirements.txt

## Estrutura final do projeto

1. **Estrutura final:**
   ```bash
   projeto_gfp/
   |-- investimentos/
   |   |-- admin.py
   |   |-- apps.py
   |   |-- migrations/
   |   |-- models.py
   |   |-- tests.py
   |   |-- views.py
   |-- usuario/
   |   |-- admin.py
   |   |-- apps.py
   |   |-- migrations/
   |   |-- models.py
   |   |-- tests.py
   |   |-- views.py
   |-- gastos/
   |   |-- admin.py
   |   |-- apps.py
   |   |-- migrations/
   |   |-- models.py
   |   |-- tests.py
   |   |-- views.py
   |-- objetivos/
   |   |-- admin.py
   |   |-- apps.py
   |   |-- migrations/
   |   |-- models.py
   |   |-- tests.py
   |   |-- views.py
   |-- relatorios/
   |   |-- admin.py
   |   |-- apps.py
   |   |-- migrations/
   |   |-- models.py
   |   |-- tests.py
   |   |-- views.py
   |-- templates/
   |   |-- ...
   |-- static/
   |   |-- ...
   |-- manage.py
   |-- requirements.txt
   |-- config/
   |   |-- settings.py
   |   |-- urls.py
   |   |-- wsgi.py

## Contribuição

Se você deseja contribuir para o projeto, siga estes passos:
1. **Faça um fork do repositório.**
2. **Crie uma branch para a sua contribuição:**
   ```bash
   git checkout -b minha-contribuicao
3. **Faça suas alterações.**
4. **Faça commit das suas alterações:**
   ```bash
   git commit -m "Descrição concisa das alterações"
5. **Envie suas alterações para o seu fork:**
   ```bash
   git push origin minha-contribuicao
6. **Abra um pull request para revisão.**

## Licença
Este projeto é licenciado sob a Licença MIT.