from config import app, db
from models import User, Event

# é necessário usar o contexto da aplicação para criar as tabelas
with app.app_context():
    db.create_all() # cria todas as tabelas definidas no models.py
    print('Banco de dados criado com sucesso!')
