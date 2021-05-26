#$env:FLASK_APP = "demo.py"
from flask import (
    Flask,
    render_template,
    request
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

@app.route("/form-ejemplo", methods=['GET','POST'])
def funcion_form():
    form = request.form
    if request.method == "POST":
        id = form.get('id') #'id' es el atributo name de los input
        tipo = form.get('tipo')
        palabra = form.get('palabra')
        def_eng = form.get('def_eng')
        #envio la informacion recibida desde el form y la envio a la misma hoja html
        return render_template('ejemplo-form.html',
            post=True,
            id = id, 
            tipo = tipo, 
            palabra = palabra, 
            def_eng = def_eng)
    print("get")
    #Si la solicitud es tipo get llego a esta instruccion
    return render_template('ejemplo-form.html',post=False)

if __name__=="__main__":
    with app.app_context():
        app.run(debug=True)


#127.0.0.1 = localhost = 0.0.0.0