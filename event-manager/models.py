from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from config import db, login_manager

# função para carregar o usuário logado
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # relacionamento: um usuário pode ter vários eventos
    events = db.relationship('Event', backref='owner', lazy=True, cascade='all, delete-orphan')

    def set_password(self, password):
        # gera o hash da senha
        self.password = generate_password_hash(password)

    def check_password(self, password):
        # verifica a senha
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Event {self.event_name} ({self.event_date})>'
