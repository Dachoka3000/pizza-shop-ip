from . import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    password_hash = db.Column(db.String(255))

    def __repr__(self):
        return f"User {self.username}"


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return f"Role {self.name}"


class Flavour(db.Model):
    __tablename__ = "flavours"

    id = db.Column(db.Integer, primary_key=True)
    pizza_flavour = db.Column(db.String(255), unique=True)
    orders = db.relationship("Order", backref="flavour", lazy="dynamic")

    def __repr__(self):
        return f"Flavour {self.pizza_flavour}"


class Size(db.Model):
    __tablename__ = "sizes"

    id = db.Column(db.Integer, primary_key=True)
    pizza_size = db.Column(db.String(255), unique=True)
    price = db.Column(db.Integer)
    orders = db.relationship("Order", backref="size", lazy="dynamic")

    def __repr__(self):
        return f"Size {self.pizza_size}"


class Topping(db.Model):
    __tablename__ = "toppings"

    id = db.Column(db.Integer, primary_key=True)
    pizza_topping = db.Column(db.String(255), unique=True)
    price = db.Column(db.Integer)
    orders = db.relationship("Order", backref="topping", lazy="dynamic")

    def __repr__(self):
        return f"Topping {self.pizza_topping}"


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    flavour_id = db.Column(db.Integer, db.ForeignKey("flavours.id"))
    size_id = db.Column(db.Integer, db.ForeignKey("sizes.id"))
    topping_id = db.Column(db.Integer, db.ForeignKey("toppings.id"))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    checkouts = db.relationship("Checkout", backref="order", lazy="dynamic")

    def __repr__(self):
        return f"Order {self.price}"


class Checkout(db.Model):
    __tablename_ = "checkouts"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    email = db.Column(db.String(255))
    total_amount = db.Column(db.Integer)

    def __repr__(self):
        return f"Checkout {self.total_amount}"
