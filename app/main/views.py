<<<<<<< HEAD
from flask import render_template, flash, session,request, redirect, url_for
from . import main
from .forms import OrderForm
from ..models import Order, Checkout, Flavour, Topping, Size
from .. import db
=======
from flask import render_template, redirect, url_for
from . import main
from .forms import FlavourForm, SizeForm, ToppingForm
from .. import db
from ..models import Flavour, Size, Topping
>>>>>>> 0a3637f44cd3c63c5e6ae94705cf6176f2f184ff


@main.route('/')
def index():
<<<<<<< HEAD
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

=======
    title = 'pizza'

    return render_template("index.html")

@main.route('/add')
def add():
    title = 'pizza details'

    return render_template("pizza_details.html")


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
>>>>>>> 0a3637f44cd3c63c5e6ae94705cf6176f2f184ff
