from flask import render_template, flash, session,request, redirect, url_for
from . import main
from .forms import OrderForm
from ..models import Order, Checkout, Flavour, Topping, Size
from .. import db


@orders.route("/")
def index():
  title = 'pizza'
  
return render_template("index.html")

@orders.route("/cart/order/<int:id>", methods=["POST","GET"])
def new_order(id):
    form = OrderForm()
    amount = 0

    if form.validate_on_submit():
        quantity = form.quantity.data 
        size = form.size.data 
        if Size.query.filter_by(pizza_size == form.size.data).first():
             size_id = sizes.id
             return size_id
        flavour = form.flavour.data 
        if Flavour.query.filter_by(pizza_flavour == form.flavour.data).first():
            flavour_id = flavours.id 
            return flavour_id
        topping = form.toppings.data 
        if Topping.query.filter_by(pizza_topping == form.toppings.data).first():
            topping_id = toppings.id
            return topping_id
        if Size.query.filter_by(pizza_size == form.size.data).first():
             price_size = sizes.price
             return price_size
        if Topping.query.filter_by(pizza_size == form.toppings.data).first():
             price_topping = toppings.price
             return price_topping

        
            price = price_size + price_topping
        new_order=Order(id,flavour_id,size_id,topping_id,quantity,price)
        db.session.add(new_order)
        db.session.commit()
        


@orders.route("/cart/checkout")
def checkout():
    id = checkouts.id 
    email = checkouts.email
    total = checkouts.total_amount

