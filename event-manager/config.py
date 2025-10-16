from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()  # carrega as variáveis do arquivo .env (se existir)

# garante que a pasta instance exista
if not os.path.exists('instance'):
    os.makedirs('instance')  # se a pasta não existir, cria

# cria o app Flask usando pasta instance
app = Flask(__name__, instance_relative_config=True)

# caminho absoluto do diretório base do projeto
basedir = os.path.abspath(os.path.dirname(__file__))

# configurações do app
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'supersecretkey')

# caminho absoluto para o arquivo SQLite dentro da pasta instance
db_path = os.path.join(basedir, 'instance', 'event_manager.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f'sqlite:///{db_path}')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # evita warnings do SQLAlchemy

# inicializa o banco de dados
db = SQLAlchemy()
db.init_app(app)

# inicializa o Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
