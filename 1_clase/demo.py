#$env:FLASK_APP = "demo.py"
from flask import (
    Flask,
    render_template
)
from datetime import datetime
import json

app = Flask(__name__) # __name__ == "__main__"

@app.route("/")
def funcion_inicio():
    return render_template('index.html')

@app.route("/fecha")
def funcion_fecha():
    return render_template('fecha.html',fecha=str(datetime.now()))

@app.route("/palabras")
def funcion_palabra():
    f = open('palabra_data.json',)
    lista = json.load(f)
    return render_template('palabra.html',lista_palabra=lista)

if __name__=="__main__":
    with app.app_context():
        app.run(debug=True)


#127.0.0.1 = localhost = 0.0.0.0