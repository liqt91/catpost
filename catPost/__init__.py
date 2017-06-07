from flask import Flask


def make_app(config=None, debug=False, port=80):
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask("catPost", instance_relative_config=True)
    app.config.from_pyfile(config)
    app.debug = debug
    configure_views(app)
    configure_extensions(app)
    return app


def configure_extensions(app):
    from catPost.extensions import db
    db.init_app(app)


def configure_views(app):
    from catPost.views import views
    for module, url_prefix in views:
        app.register_blueprint(module, url_prefix=url_prefix)