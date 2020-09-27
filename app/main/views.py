from flask import render_template, flash, session,request, redirect, url_for
from . import main
from .forms import OrderForm
from ..models import Order, Checkout, Flavour, Topping, Size
from .. import db


@main.route("/")
def index():
  title = 'pizza'
  
  return render_template("index.html", title=title)

@main.route("/cart/order", methods=["POST","GET"])
def new_order():
    form = OrderForm()

    if form.validate_on_submit():
        quantity = form.quantity.data 
        size = form.size.data 
        flavour = form.flavour.data 
        topping = form.toppings.data 
        price = ((int(size.price))+(int(topping.price))*(int(quantity)))
        new_order=Order(flavour=flavour,size=size,topping=topping,quantity=quantity,price=price)
        db.session.add(new_order)
        db.session.commit()
        
    return render_template("cart.html", order_form = form,)

