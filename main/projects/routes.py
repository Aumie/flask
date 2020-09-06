from flask import render_template, request, Blueprint

projects = Blueprint('projects', __name__)



@projects.route("/projects/proj<int:projid>")
def home(projid):
    return render_template('proj{}.html'.format(projid))
