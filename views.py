from flask import render_template,Blueprint

views = Blueprint("views", __name__)

@views.route("/")
def homepage():
    return render_template("base.html")