from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required

class FlavourForm(FlaskForm):
    flavour123 = StringField('Pizza flavour')
    submit = SubmitField('Submit')
    
class SizeForm(FlaskForm):
    pizza_size = StringField('Pizza size')
    pizza_size_price = IntegerField('Size price') #remember to convert to integer
    submit = SubmitField('Submit')
    
class ToppingForm(FlaskForm):
    pizza_topping = StringField('Pizza topping')
    pizza_topping_price = IntegerField('Topping price') #remember to convert to integer
    submit = SubmitField('Submit')