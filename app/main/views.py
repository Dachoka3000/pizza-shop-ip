from flask import render_template
from . import main


@main.route("/")
def index():
  title = 'pizza'
  
  return render_template("index.html")