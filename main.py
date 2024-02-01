from flask import Flask, render_template, request
from form import DistanciaForm

app = Flask(__name__)

@app.route("/OperasBas")
def operaciones():
    return render_template("operasBas.html")

@app.route("/resultado", methods=["GET","POST"])
def resultado():
    if request.method == "POST":
        n1=int(request.form["n1"])
        n2=int(request.form["n2"])
        operacion = request.form["operacion"]
        if operacion == "suma":
            return f"La suma de {n1} + {n2} es {n1+n2}"
        elif operacion == "resta":
            return f"La resta de {n1} - {n2} es {n1-n2}"
        elif operacion == "multi":
            return f"La multiplicacion de {n1} * {n2} es {n1*n2}"
        elif operacion == "div":
            return f"La division de {n1} / {n2} es {n1/n2}"
        
@app.route("/distancia", methods=["GET","POST"])
def distancia():
    distanciaClase = DistanciaForm(request.form)
    x1=0
    x2=0
    y1=0
    y2=0
    resultado=0

    if request.method == "POST":
        x1 = distanciaClase.x1.data
        x2 = distanciaClase.x2.data
        y1 = distanciaClase.y1.data
        y2 = distanciaClase.y2.data
        
        resultado = ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    return render_template("distancia.html", form=distanciaClase, resultado=resultado)
    
if __name__ == "__main__":
    app.run(debug=True) 