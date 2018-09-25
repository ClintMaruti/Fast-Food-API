from flask import Flask
from flask_restful import Api

#local imports
import config

from app.resources.order_resources import OrderResources
from app.resources.order_resources import SpecificOrder
from app.resources.order_resources import Views

def create_app(config_name):
    '''Function that creates flask app depending on the configuration passed'''
    
    #initialize flask app
    app = Flask(__name__)

    #initialize api 
    api = Api(app)

    app.config.from_object('config')
    app.url_map.strict_slashes = False

 

    #register endpoints
    api.add_resource(Views, '/')
    api.add_resource(OrderResources, '/api/v1/orders/')
    api.add_resource(SpecificOrder,'/api/v1/orders/<int:order_id>' )

    return app
