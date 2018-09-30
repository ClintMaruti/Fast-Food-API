from flask import Flask
from flask_restful import Api

#local imports
from config import app_config
from db import connect

from app.resources.order_resources import OrderResources
from app.resources.order_resources import SpecificOrder
from app.resources.order_resources import Views

#challenge 3 imports
from app.resources.v2.resources.users.orders import OrderResourcesV2
# from app.resources.v2.resources.users. import ViewsV2
# from app.resources.v2.resources.views import SpecificOrderV2
from app.resources.v2.resources.users.user import UserResource
from app.resources.v2.resources.users.user import UserLogin
from app.resources.v2.resources.users.menu import MenuResources


def create_app(config_name):
    '''Function that creates flask app depending on the configuration passed'''
    
    #initialize flask app
    app = Flask(__name__)

    #initialize api 
    api = Api(app)

    app.config.from_pyfile('config.py')
    #app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False

 
    connect()

    #register endpoints challenge 2
    api.add_resource(Views, '/')
    api.add_resource(OrderResources, '/api/v1/orders/')
    api.add_resource(SpecificOrder,'/api/v1/orders/<int:order_id>' )

    #register endpoints for challenge 3
    # api.add_resource(ViewsV2,'/')
    api.add_resource(OrderResourcesV2, '/api/v2/orders/')
    # api.add_resource(SpecificOrderV2,'/api/v2/orders/')

    #register endpoiny for challenge 3 user
    api.add_resource(UserResource,'/api/v2/users/')
    api.add_resource(UserLogin, '/api/v2/users/')
    api.add_resource(MenuResources, '/api/v2/menu/')

    return app
