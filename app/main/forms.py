from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField
from wtforms.validators import Required

class OrderForm(FlaskForm):
    size = StringField('size', validators=[Required])
    flavour = StringField('flavour', validators=[Required])
    toppings = TextAreaField('toppings', validators=[Required])
    quantity = StringField('quantity',validators=[Required])
    submit = SubmitField('Submit')