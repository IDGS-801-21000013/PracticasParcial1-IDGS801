from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, RadioField


class ResistenciaForm(Form):
    b1= SelectField("Banda 1", choices=['Negro', 'Cafe','Naranja', 'Rojo', 'Amarillo', 'Verde', 'Azul','Violeta', 'Gris', 'Blanco'], default="Negro")
    b2= SelectField("Banda 2", choices=['Negro', 'Cafe', 'Naranja', 'Rojo', 'Amarillo', 'Verde', 'Azul','Violeta', 'Gris', 'Blanco'], default="Negro")
    b3= SelectField("Banda 3", choices=['Negro', 'Cafe','Naranja',  'Rojo', 'Amarillo', 'Verde', 'Azul','Violeta', 'Gris', 'Blanco'], default="Negro")
    t= RadioField('Tolerancia', choices=['Oro','Plata'], default="Oro")

class DistanciaForm(Form):
    x1=IntegerField("x1")    
    x2=IntegerField("x2")
    y1=IntegerField("y1")
    y2=IntegerField("y2")




    

