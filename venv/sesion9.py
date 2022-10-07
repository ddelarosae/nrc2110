from flask import Flask, render_template, request, flash, jsonify
from mensaje import mensajes
import yagmail
import utils
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
@app.route('/')
def index():
    return render_template('register.html')
@app.route('/login', methods=('GET','POST'))
def login():
    try:
        return jsonify(mensajes)
    except:
        return render_template('error.html')

@app.route('/error')
def error():
    return render_template('error.html')
@app.route('/register', methods=('GET','POST'))
def register():
    try:
        if request.method == 'POST':
            username = request.form['usuario']
            password = request.form['pass']
            email = request.form['correo']
            error=None
            if not utils.isUsernameValid(username):
                error="revisar usuario"
                flash(error)
                return render_template('register.html')

            if not utils.isPasswordValid(password):
                error="revisar contraseña"
                flash(error)
                return render_template('register.html')
        
            if not utils.isEmailValid(email):
                error="revisar correo"
                flash(error)
                return render_template('register.html')

            correo_electronico=yagmail.SMTP('danieldelarosa.ruta1@utp.edu.co','Qn$w+?3x.ACg') #correo electronico es la variable que almacena el correo y la contraseña
            correo_electronico.send(
                to=email,
                subject='Cuenta activada',
                contents='Bienvenido al sistema diseñado por el grupo 2110'
            )
            flash('Te hemos enviado un correo')
            return render_template('login.html')
        return render_template('register.html')
    except:
        return render_template('error.html')