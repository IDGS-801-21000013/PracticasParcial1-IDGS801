from wtforms import Form
from wtforms import validators
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, RadioField, StringField,SubmitField


from wtforms.validators import DataRequired, Email, Length


class ResistenciaForm(Form):
    b1= SelectField("Banda 1", choices=['Negro', 'Cafe','Naranja', 'Rojo', 'Amarillo', 'Verde', 'Azul','Violeta', 'Gris', 'Blanco'], default="Negro")
    b2= SelectField("Banda 2", choices=['Negro', 'Cafe', 'Naranja', 'Rojo', 'Amarillo', 'Verde', 'Azul','Violeta', 'Gris', 'Blanco'], default="Negro")
    b3= SelectField("Banda 3", choices=['Negro', 'Cafe','Naranja',  'Rojo', 'Amarillo', 'Verde', 'Azul','Violeta', 'Gris', 'Blanco'], default="Negro")
    t= RadioField('Tolerancia', choices=['Oro','Plata'], default="Oro")

class WriteReadText(Form):
    ingles = StringField("Ingles",[validators.DataRequired(message="Campo requerido"), validators.length(min=3,max=20,message="Escribe un texto valido")])
    espanol = StringField("Español",[validators.DataRequired(message="Campo requerido"), validators.length(min=4,max=20,message="Escribe un texto valido")]) 
    radio = RadioField('', choices=['Español','Ingles'], default='Español') 
    buscar = StringField("Buscar", [validators.DataRequired(message="Campo requerido"), validators.length(min=3,max=20,message="Escribe un texto valido")],default="")
    escribir = SubmitField("")
    leer = SubmitField("")

class DistanciaForm(Form):
    x1=IntegerField("x1")    
    x2=IntegerField("x2")
    y1=IntegerField("y1")
    y2=IntegerField("y2")




    

