Blog Simples — Desafio Django
-----------------------------------------------------------------------------------------------

Projeto desenvolvido como parte do desafio de seleção de bolsistas.
Aplicação web construída com Django e PostgreSQL que implementa um sistema de blog simples.
Funcionalidades:

- Cadastro de autores, categorias, tags e posts via Django Admin 
- O site público exibe os posts e permite comentários.
- Interface baseada em template externo com Bootstrap 5

-----------------------------------------------------------------------------------------------

Requisitos/Tecnologias Utilizadas:

    Python 3.10+ (ou 3.8+)
    pip
    PostgreSQL 12+
    Bootstrap 5.3(via CDN)
    Django 6.0.2
    virtualenv
    psycopg2-binary 
    python-decouple

Obs:O Bootstrap é importado via CDN, então é necessária conexão com a internet

----------------------------------------------------------------------------------------------

Configuração local (modo manual):

1. Clone o repositório:
   
    git clone https://github.com/Artuyr/blog.git
   
    cd blog

2. Crie e ative um ambiente virtual:
   
    python -m venv .venv
   
    source .venv/bin/activate # Linux / macOS
   
    .venv\Scripts\activate # Windows PowerShell

3. Instale dependências:
   
    pip install -r requirements.txt

4. Crie um banco de dados e usuário no PostgreSQL:
   
    CREATE DATABASE blogdb;

    CREATE USER blog_user WITH ENCRYPTED PASSWORD 'sua_senha';
   
    GRANT ALL PRIVILEGES ON DATABASE blogdb TO blog_user;

5.Crie um arquivo .env com:
    
    SECRET_KEY="sua_key"
    DEBUG=True

    DB_NAME=blogdb
    DB_USER=blog_user
    DB_PASSWORD="sua_senha"
    DB_HOST=localhost
    DB_PORT=5432

Obs¹:Para gerar uma chave secreta aleatória: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Obs²:Para entrar em modo de produção: DEBUG=False

6. Aplique migrações e colete estáticos:
   
    python manage.py migrate
   
    python manage.py collectstatic --noinput

7. Crie um superusuário (para acessar admin e semear dados):
   
    python manage.py createsuperuser

8. Rode o servidor:
    
    python manage.py runserver

9. Semeie os dados:

   Acesse: http://127.0.0.1:8000/admin/

   Faça Login com o superusuário criado anteriormente

   Cadastre Autores, Categorias, Tags e Posts

10. Visualize o blog público:

    Acesse: http://127.0.0.1:8000
