from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField,SubmitField
from wtforms.validators import Required
from ..models import Flavour,Size,Topping,Order

class OrderForm(FlaskForm):
    size = StringField('Enter pizza size', validators=[Required])
    flavour = StringField('Enter flavour', validators=[Required])
    toppings = TextAreaField('Enter toppings', validators=[Required])
    quantity = IntegerField('quantity',validators=[Required])
    submit = SubmitField('Submit')