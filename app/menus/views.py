from .forms import OrderForm
from flask import render_template, flash, session,request, redirect, url_for
from . import orders
from ..models import Order, Checkout, Flavour, Topping, Size
from .. import db


# @orders.route("/cart")
# def index():
#   title = 'pizza'
#   form = OrderForm()
  
#   return render_template("cart.html")

@orders.route("/cart/order", methods=["POST","GET"])
def new_order():

    form = OrderForm()
    if form.validate_on_submit():
        quantity = int(form.quantity.data) 
        size = form.size.data 
        flavour = form.flavour.data 
        topping = form.toppings.data 
        price = ((int(size.price))+(int(topping.price)))*(int(quantity))
        email = form.email.data

        new_order=Order(flavour=flavour,size=size,topping=topping,quantity=quantity,price=price)
        db.session.add(new_order)
        db.session.commit()

        new_checkout = Checkout()



    title = "Orders"
        

    return render_template('cart.html', order_form = form, title = title)
# @orders.route("/cart/checkout")
# def checkout():
#     id = checkouts.id 
#     email = checkouts.email
#     total = checkouts.total_amount

