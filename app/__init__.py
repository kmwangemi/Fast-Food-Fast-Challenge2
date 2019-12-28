from flask import Flask

import os
from instance.config import app_config
from app.api.v1.views.order_view import order

def create_app(config_name):
    '''configuring the Flask App'''
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])

    app.register_blueprint(order)
  
    return app