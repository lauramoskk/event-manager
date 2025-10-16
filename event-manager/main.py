from flask import render_template, redirect, url_for, flash, request
from config import app, db
from models import User, Event
from flask_login import login_user, logout_user, current_user, login_required
from forms import RegisterForm, LoginForm, EventForm
from werkzeug.security import generate_password_hash, check_password_hash

# página inicial
@app.route('/')
def home():
    return render_template('index.html')

# registro de usuários
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # verifica se o usuário já existe
        if User.query.filter_by(username=username).first():
            flash('Usuário já existe!', 'warning')
        else:
            # cria um novo usuário caso não exista e salva no banco
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()

            flash('Usuário criado com sucesso!', 'success')
            return redirect(url_for('login'))

    return render_template('register.html', form=form)

# login de usuários
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuário ou senha incorretos.', 'danger')

    return render_template('login.html', form=form)

# logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi deslogado.', 'info')
    return redirect(url_for('login'))

# dashboard do usuário
@app.route('/dashboard')
@login_required
def dashboard():
    # mostra apenas os eventos do usuário logado
    user_events = Event.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', events=user_events)

# criar evento
@app.route('/create_event', methods=['GET', 'POST'])
@login_required
def create_event():
    form = EventForm()

    if form.validate_on_submit():
        # verifica se o usuário já criou um evento com o mesmo nome
        if Event.query.filter_by(event_name=form.event_name.data, user_id=current_user.id).first():
            flash('Você já criou um evento com esse nome.', 'warning')
        else:
            new_event = Event(
                event_name=form.event_name.data,
                event_date=form.event_date.data,
                description=form.description.data,
                user_id=current_user.id
            )
            db.session.add(new_event)
            db.session.commit()
            flash('Evento criado com sucesso!', 'success')
            return redirect(url_for('dashboard'))

    return render_template('create_event.html', form=form)

# editar evento
@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
@login_required
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)

    if event.owner != current_user:
        flash('Acesso negado.', 'danger')
        return redirect(url_for('dashboard'))

    form = EventForm(obj=event)

    if form.validate_on_submit():
        event.event_name = form.event_name.data
        event.event_date = form.event_date.data
        event.description = form.description.data
        db.session.commit()
        flash('Evento atualizado com sucesso!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('edit_event.html', form=form)

# deletar evento
@app.route('/delete_event/<int:event_id>', methods=['POST'])
@login_required
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    
    if event.owner != current_user:
        flash('Acesso negado.', 'danger')
    else:
        db.session.delete(event)
        db.session.commit()
        flash('Evento deletado com sucesso!', 'success')

    return redirect(url_for('dashboard'))

# rodar aplicação
if __name__ == '__main__':
    app.run(debug=True)
