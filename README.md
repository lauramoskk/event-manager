# Gerenciador de Eventos

### Descrição

O Gerenciador de Eventos é uma aplicação web desenvolvida em Python utilizando o framework Flask, com o objetivo de permitir que usuários criem e gerenciem seus próprios eventos de maneira prática e organizada.

A aplicação foi construída com foco em demonstrar conceitos fundamentais de desenvolvimento web, como autenticação de usuários, persistência de dados, validação de formulários e controle de acesso, servindo como um excelente exemplo de aplicação CRUD (Create, Read, Update, Delete).

Cada usuário pode registrar uma conta, fazer login e acessar seu próprio painel de controle (dashboard), onde é possível criar, editar e excluir eventos pessoais. O sistema garante que cada usuário tenha acesso apenas aos seus próprios dados, utilizando autenticação via Flask-Login e criptografia de senha com Werkzeug Security, assegurando uma camada de proteção contra acessos indevidos.

<br>

### Instruções de execução

1. Clone o repositório e acesse a pasta:
<br>git clone https://github.com/seu-usuario/event-manager.git
<br>cd event-manager

2. Instale as dependências necessárias:
<br>pip install Flask Flask-Login Flask-WTF Flask-SQLAlchemy WTForms python-dotenv

3. Criar o banco de dados
<br>O sistema utiliza um banco de dados SQLite localizado dentro da pasta instance/.
<br>Para criar o banco, execute o seguinte comando:
<br>python create_database.py

4. Executar a aplicação
<br>Com o banco de dados criado, inicie o servidor Flask:
<br>python main.py

5. Abra o navegador e acesse: http://127.0.0.1:5000/
