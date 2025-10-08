from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)


personaje = {
    "nombre": "El diablo",
    "edad": 666,
    "hobbies": ["Borra codigos", "reír maléficamente", "Se come a los estudiantes"]
}

@app.route("/")
def hola_mundo():
    return "<h1>👻 ¡Buuu! Dulce o Puntos 🎃</h1>"

@app.route("/personaje")
def personaje_json():
    datos = {
        "nombre": personaje["nombre"],
        "edad": personaje["edad"],
        "hobbies": ", ".join(personaje["hobbies"])
    }
    return jsonify(datos)

@app.route("/invocar")
def mostrar_personaje():
    return render_template('pagina.html', person=personaje)