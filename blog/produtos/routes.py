import json
from flask import redirect, render_template, url_for, flash, request,jsonify

from blog import db, app
from .models import Marca, Categoria

@app.route('/api/addmarca', methods=['GET', 'POST'])

def addmarca():
    if request.method == "POST":
        getmarca = request.form.get('marca')
        marca = Marca(name=getmarca)
        db.session.add(marca)
        flash(f'A marca {getmarca} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('addmarca'))
    return render_template('produtos/addmarca.html', marcas = 'marcas' )

@app.route('/api/listarMarcas', methods=['GET'])
def listarMarcas():
    marca = db.session.query(Marca)
    
        

    return  "Nada por enquantoo"