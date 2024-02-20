from flask import Flask, render_template, request
from form import DistanciaForm, ResistenciaForm, WriteReadText
from io import open, IOBase

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

@app.route("/resistencia", methods=["GET","POST"])
def resistencia():
    form = ResistenciaForm(request.form)
    b1='Negro'
    b2='Negro'
    b3='Negro'
    t='Oro'
    oms=0
    omsMax=0
    omsMin=0
    c1=0
    c2=0
    mult=0
    tol=0
    col1='White'
    col2='White'
    col3='White'

    if request.method == "POST":
        b1 = form.b1.data        
        b2 = form.b2.data
        b3 = form.b3.data
        t = form.t.data    
    
        vResistencia = {
        'Negro': 0,
        'Cafe': 1,
        'Rojo': 2,
        'Naranja': 3,
        'Amarillo': 4,
        'Verde': 5,
        'Azul': 6,
        'Violeta': 7,
        'Gris': 8,
        'Blanco': 9
        }

        bg = {
        'Negro': 'Black',
        'Cafe': 'Brown',
        'Rojo': 'Red',
        'Naranja': 'Orange',
        'Amarillo': 'Yellow',
        'Verde': 'Green',
        'Azul': 'Blue',
        'Violeta': 'Purple',
        'Gris': 'Gray',
        'Blanco':'White',
        'Oro':'#FFD700',
        'Plata':'#BEBEBE',
        }

        multiplicando = {
        'Negro': 1,
        'Cafe': 10,
        'Rojo': 100,
        'Naranja': 1000,
        'Amarillo': 10000,
        'Verde': 100000,
        'Azul': 1000000,
        'Violeta': 10000000,
        'Gris': 100000000,
        'Blanco': 1000000000,
        }
            
        tolerancia={
        'Oro':0.05,
        'Plata': 0.1
        }

        c1 = vResistencia[b1]
        c2 = vResistencia[b2]
        col1 = bg[b1]
        col2= bg[b2]
        col3= bg[b3]
        col4=bg[t]
        print(t)
        print(col4)
        mult = multiplicando[b3]
        tol = tolerancia[t]
        
        oms = int(str(c1) + str(c2)) * mult
        omsMax = oms + (oms * tol)
        omsMin = oms - (oms * tol)
        
        return render_template('resistencia.html', form=form, b1=b1, b2=b2, b3=b3, t=t, oms=oms, omsMax=omsMax, omsMin=omsMin, tol=tol, c1=c1, c2=c2, mult=mult, col1=col1, col2=col2, col3=col3, col4=col4)
    
    return render_template('resistencia.html', form=form)

@app.route('/archivos', methods=["GET", "POST"])
def EscrText():
    form = WriteReadText(request.form)
    file_content = ""
    palabra_encontrada = ""

    if request.method == "POST":
        ingles = form.ingles.data
        espanol = form.espanol.data
        buscar = form.buscar.data
        radio = form.radio.data

        if form.escribir.data and form.escribir.validate(form):
            with open('diccionario.txt', 'a') as file:
                file.write(f"{ingles}:{espanol},\n")

            form.ingles.data = ""
            form.espanol.data = ""
        
        elif form.leer.data and form.leer.validate(form):  
                with open('diccionario.txt', 'r') as file:
                    file_content = file.read()
                    for line in file_content.split(','):
                        print(line)
                        if buscar in line:
                            clave, valor = line.split(':')
                            if radio == "Español":
                                palabra_encontrada = clave
                            elif radio == "Ingles":
                                palabra_encontrada = valor
                            break
                        else:
                            palabra_encontrada = f"No se encontro la palabra {buscar}"  

        form.buscar.data = ""  

        return render_template('archivos.html', form=form, ingles=ingles, espanol=espanol, radio=radio, buscar=buscar,
                                file_content=file_content, palabra_encontrada=palabra_encontrada)

    return render_template('archivos.html', form=form)


def buscar_en_archivo(texto, contenido):
    lineas = contenido.split('\n')
    resultados = [linea for linea in lineas if texto.upper() in linea.upper()]
    return '\n'.join(resultados)


if __name__ == "__main__":
    app.run(debug=True) 
