from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import IntegerField


class DistanciaForm(Form):
    x1=IntegerField("x1")    
    x2=IntegerField("x2")
    y1=IntegerField("y1")
    y2=IntegerField("y2")
    

