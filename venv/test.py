from flask import Flask, jsonify	
from productos import productos
app = Flask(__name__) 
@app.route('/api')
def api():
    return jsonify({"message":"Hola Mundo!"})
@app.route('/productos')
def getProductos():
    return jsonify(productos)
@app.route('/articulos/<string:nom_articulo>')
def getArticulo(nom_articulo):
    encontrado = [articulo for articulo in productos if articulo['nombre'] == nom_articulo] 
    if (len(encontrado) > 0):
        return jsonify({"articulo": encontrado[0]})
    return jsonify({"message":"Articulo no encontrado"})

