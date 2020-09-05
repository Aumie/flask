from flask import Flask


def create_app():
    app = Flask(__name__)

    from main.home.routes import main
    from main.projects.routes import projects
    from main.errors.handler import errors

    app.register_blueprint(main)
    app.register_blueprint(projects)
    app.register_blueprint(errors)

    return app
