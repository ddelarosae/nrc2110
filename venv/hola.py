from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h2>Hola tripulantes MINTIC 2022-2, saldudos de su profesor</h2>"