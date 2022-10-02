from flask import render_template, session, request, url_for, flash, redirect

from .form import LoginFormulario, RegistrationForm

from blog import app, db, bcrypt
from .models import User
import os



@app.route('/home')
def home():
    return render_template('admin/index.html')


@app.route('/admin')

def admin():
    if 'email' not in session:
        flash('Fazer o login é necessário ao entrar no sistema', 'danger')
        return redirect(url_for('login'))
    return render_template('admin/index.html')


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(nome=form.name.data, email=form.email.data,
        password = hash_password)
        
        db.session.add(user)
        db.session.commit()
        flash(f'Obrigado {form.name.data} por registrar', 'success')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title= "Pagina de registro")

# rota do login
@app.route('/login', methods=['GET', 'POST'])

def login():
    form =LoginFormulario(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Olá {form.email.data}, Você está logado', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('Não foi possível logar no sistema.')
    return render_template('admin/login.html', form=form, title='Pagina login')
    

