from flask import Flask, render_template, request

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

    
if __name__ == "__main__":
    app.run(debug=True) 