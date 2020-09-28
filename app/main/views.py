
from flask import render_template, flash, session,request, redirect, url_for
from . import main
from .forms import OrderForm
from ..models import Order, Checkout, Flavour, Topping, Size
from .. import db
from .forms import FlavourForm, SizeForm, ToppingForm
from ..email import mail_message
# from sqlalchemy import desc

@main.route('/')
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
      price = ((int(size.price))+(int(topping.price)))*(int(quantity))
      new_order=Order(flavour=flavour,size=size,topping=topping,quantity=quantity,price=price)

      db.session.add(new_order)
      db.session.commit()
      email = form.email.data

      mail_message("Thank you customer","email/order_received",email,new_order=new_order)
      flash("Your order has been recorded")
  else:
      flash("Sorry, I really didn't get that")
        
  title = 'Orders'

  return render_template("cart.html", order_form = form, title=title)



@main.route("/cart/order/checkout")
def new_checkout():


  title='Checkout'

  return render_template("checkout.html", title=title)

@main.route('/add')
def add():
    title = 'pizza details'

    return render_template("pizza_details.html", title = title)


@main.route('/add/flavour', methods=["GET", "POST"])
def newFlavour():
    flavour_form = FlavourForm()
    
    
    if flavour_form.validate_on_submit():
        flavour = Flavour(pizza_flavour=flavour_form.pizza_flavour.data)
        db.session.add(flavour)
        db.session.commit()

    return render_template('add_flavour.html', flavour_form=flavour_form)

@main.route('/add/size', methods=["GET", "POST"])
def newSize():
    size_form = SizeForm()
    
    if size_form.validate_on_submit():
        size = Size(pizza_size=size_form.pizza_size.data, price= size_form.pizza_size_price.data)
        db.session.add(size)
        db.session.commit()

    return render_template('add_size.html', size_form=size_form)


          
@main.route('/add/topping', methods=["GET", "POST"])
def newTopping():
    topping_form = ToppingForm()
    
    if topping_form.validate_on_submit():
        topping = Topping(pizza_topping=topping_form.pizza_topping.data, price=topping_form.pizza_topping_price.data)
        db.session.add(topping)
        db.session.commit()
        
    return render_template('add_topping.html', topping_form=topping_form)
