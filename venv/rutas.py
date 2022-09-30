from flask import Flask,render_template, redirect, url_for, flash
from form import FormInicio
import os
SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
@app.route('/')
def inicio():
    return render_template('base.html')
@app.route('/index')
def index():
    usuario = {'usuario':'...'}
    comentarios = [
        {'autor':{'usuario':'...'}, 'comentario':'...'},
        {'autor':{'usuario':'...'}, 'comentario':'...'}
    ]
    return render_template('index.html', titulo='Inicio', usuario=usuario, comentarios=comentarios)
@app.route('/login',methods=['GET', 'POST'])
def login():
    form = FormInicio()
    if(form.validate_on_submit()):
        flash('Inicio de sesión solicitado por el usuario {}, recordar={}'.format(form.usuario.data,form.recordar.data))
        return redirect(url_for('gracias'))
    return render_template('iniciar_sesion.html', form=form)
@app.route('/gracias')
def gracias():
    return render_template('gracias.html')