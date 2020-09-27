from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired
from ..models import Flavour,Size,Topping,Order
from .. import db

def flavour_query():
    return Flavour.query

def size_query():
    return Size.query

def topping_query():
    return Topping.query

class OrderForm(FlaskForm):
    size = QuerySelectField(query_factory=size_query, allow_blank = True)
    flavour = QuerySelectField(query_factory=flavour_query, allow_blank=True)
    toppings = QuerySelectField(query_factory=topping_query, allow_blank=True)
    quantity = IntegerField('quantity',validators=[InputRequired()])
=======
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required

class FlavourForm(FlaskForm):
    pizza_flavour = StringField('Pizza flavour')
    submit = SubmitField('Submit')
    
class SizeForm(FlaskForm):
    pizza_size = StringField('Pizza size')
    pizza_size_price = IntegerField('Size price') #remember to convert to integer
    submit = SubmitField('Submit')
    
class ToppingForm(FlaskForm):
    pizza_topping = StringField('Pizza topping')
    pizza_topping_price = IntegerField('Topping price') #remember to convert to integer
>>>>>>> 0a3637f44cd3c63c5e6ae94705cf6176f2f184ff
    submit = SubmitField('Submit')