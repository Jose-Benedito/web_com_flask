from flask import render_template, session, request, url_for, flash, redirect

from form import RegistrationForm

from blog import app, db, bcrypt
from .models import User
import os






@app.route('/')

def home():
    return 'Seja bem vindo ao blog'


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(nome=form.name.data, username=form.username.data, email=form.email.data,
        password=hash_password)
        
        db.session.add(user)
        flash('Obrigado por registrar')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form)

