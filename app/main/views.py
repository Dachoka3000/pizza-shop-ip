from flask import redirect, render_template,url_for,flash,request
from . import db 


@main.route('/')
def index():
    return render_template('index.html')

def order():
    itemid = order.id
    flavor = order.flavor_id
    size = order.size_id
    topping = order.topping_id
    price = order.price
    db.session.add(order)
    db.session.commit()
@main.route('/cart', methods=['GET','POST'])
def cart():
    return render_template('cart.html')

@main.route('/addmenu',methods = ['GET','POST'])
def addmenu():
    return render_template('menus/pizzas.html')

@main.route('/checkout')
def checkout():
    id = checkout.id
    order =Checkout(order_id)
    total = checkout.total_amount
    email= checkout.email
    db.session.add(checkout)
    db.session.commit()

