from flask import render_template, request, Blueprint

main = Blueprint('home', __name__)


@main.route("/")
def home():
    return render_template('index.html')
