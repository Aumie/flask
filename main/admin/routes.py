from flask import render_template, request, Blueprint

admin = Blueprint('admin', __name__)



@admin.route("/aumiejae")
def aumiejae():
    return render_template('aumiejae.html')
