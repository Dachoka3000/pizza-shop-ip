from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import IntegerField, SubmitField, StringField
from wtforms.validators import InputRequired
from ..models import Flavour,Size,Topping,Order,Checkout
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
    email = StringField("Enter your email", validators=[InputRequired()])
    submit = SubmitField('Submit')

# class CheckoutForm(FlaskForm):
#     email = StringField("Enter your email", validators=[InputRequired()])
#     submit = SubmitField('Submit')
