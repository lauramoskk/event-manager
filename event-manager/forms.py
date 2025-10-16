from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length

# formulário de registro de usuário
class RegisterForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(), Length(min=4, max=25)]) 
    password = PasswordField('Senha', validators=[DataRequired()]) 
    submit = SubmitField('Registrar')

# formulário de login de usuário
class LoginForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')

# formulário para criação/edição de eventos
class EventForm(FlaskForm):
    event_name = StringField('Nome', validators=[DataRequired(), Length(max=25)])
    event_date = DateField('Data', format='%Y-%m-%d', validators=[DataRequired()])
    description = TextAreaField('Descrição', validators=[DataRequired(), Length(max=70)])
    submit = SubmitField('Criar Evento')
