# app/__init__.py

from flask import Flask


def create_app():
    # Initialize the app
    app = Flask(__name__, instance_relative_config=True)
    # Load the config file
    app.config.from_object('config')

    # Load the views
    from app.views import html
    from app.orders_resource import orders_

    app.register_blueprint(html)
    app.register_blueprint(orders_)

    return app
