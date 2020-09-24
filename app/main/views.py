from flask import render_template


@main.route("/")
def index():
  title = 'pizza'
  
  return render_template("index.html")