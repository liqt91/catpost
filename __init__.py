from flask import Flask
from views import views



def make_app(config=None, debug=False, port=80):
    app = Flask(__name__)
    # app.config.from_pyfile(config)
    app.debug = debug
    configure_blueprints(app, views)
    return app


def configure_blueprints(app, modules):
    for module, url_prefix in modules:
        app.register_blueprint(module, url_prefix=url_prefix)
