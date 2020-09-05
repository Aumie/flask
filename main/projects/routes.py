from flask import render_template, request, Blueprint

projects = Blueprint('projects', __name__)



@projects.route("/projects/proj<int:projid>")
def home(projid):
    print('proj{}.html'.format(projid))
    return render_template('proj{}.html'.format(projid))
