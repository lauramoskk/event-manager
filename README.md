# Gerenciador de Eventos

### Descrição

O Gerenciador de Eventos é uma aplicação web desenvolvida em Python utilizando o framework Flask, com o objetivo de permitir que usuários criem e gerenciem seus próprios eventos de maneira prática e organizada.

A aplicação foi construída com foco em demonstrar conceitos fundamentais de desenvolvimento web, como autenticação de usuários, persistência de dados, validação de formulários e controle de acesso, servindo como um excelente exemplo de aplicação CRUD (Create, Read, Update, Delete).

Cada usuário pode registrar uma conta, fazer login e acessar seu próprio painel de controle (dashboard), onde é possível criar, editar e excluir eventos pessoais. O sistema garante que cada usuário tenha acesso apenas aos seus próprios dados, utilizando autenticação via Flask-Login e criptografia de senha com Werkzeug Security, assegurando uma camada de proteção contra acessos indevidos.

<br> 

<img width="400" height="953" alt="home" src="https://github.com/user-attachments/assets/02d608ce-9757-4185-bb21-d696e46beb3d" />
<img width="400" height="953" alt="register" src="https://github.com/user-attachments/assets/686c1fdf-c75b-434a-b932-06b883c8aed1" />
<img width="400" height="951" alt="login" src="https://github.com/user-attachments/assets/7d5b6681-f782-4934-985d-c46b3909f4ba" />
<img width="400" height="951" alt="dashboard" src="https://github.com/user-attachments/assets/13cfd20c-ebf9-4213-963e-4ecd91a89885" />
<img width="400" height="951" alt="create_event" src="https://github.com/user-attachments/assets/9dd64afd-d704-4219-8353-63285657e044" />
<img width="400" height="950" alt="edit_event" src="https://github.com/user-attachments/assets/8972222e-4e29-4153-9f87-471e664a835a" />
<img width="400" height="1040" alt="db_users" src="https://github.com/user-attachments/assets/27bfb431-9ca7-42e7-8f5d-0ef5b7490aff" />
<img width="400" height="1040" alt="db_events" src="https://github.com/user-attachments/assets/2527088a-99dd-4155-b873-ad185dbdc595" />

<br>
<br>
<br>

### Instruções de execução

```bash
# 1. Clone o repositório e acesse a pasta:
git clone https://github.com/seu-usuario/event-manager.git
cd event-manager

# 2. Instale as dependências necessárias:
pip install Flask Flask-Login Flask-WTF Flask-SQLAlchemy WTForms python-dotenv

# 3. Criar o banco de dados
# O sistema utiliza um banco de dados SQLite localizado dentro da pasta instance/.
# Para criar o banco, execute o seguinte comando:
python create_database.py

# 4. Executar a aplicação
# Com o banco de dados criado, inicie o servidor Flask:
python main.py

# 5. Abra o navegador e acesse: http://127.0.0.1:5000/
```

