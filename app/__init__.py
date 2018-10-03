from flask import Flask
from flask_restful import Api
#local imports
from config import app_config
from db import connect
import os

#challenge 2 imports
# from app.resources.order_resources import OrderResources
# from app.resources.order_resources import SpecificOrder
# from app.resources.order_resources import Views

#challenge 3 imports
from app.resources.v2.resources.endpoints.orders import OrderResourcesV2
# from app.resources.v2.resources.endpoints. import ViewsV2
from app.resources.v2.resources.endpoints.orders import OrderSpecificResourcesV2
from app.resources.v2.resources.endpoints.user import User
from app.resources.v2.resources.endpoints.user import UserResource
from app.resources.v2.resources.endpoints.user import UserLogin
from app.resources.v2.resources.endpoints.menu import MenuResources
from app.resources.v2.resources.endpoints.user import GetAllUsersResources



def create_app(config_name):
    '''Function that creates flask app depending on the configuration passed'''
    
    #initialize flask app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config)
    

    #initialize api 
    api = Api(app)

    app.url_map.strict_slashes = False
 
    connect()

    #register endpoints challenge 2
    # api.add_resource(Views, '/')
    # api.add_resource(OrderResources, '/api/v1/orders/')
    # api.add_resource(SpecificOrder,'/api/v1/orders/<int:order_id>' )

    #register endpoints for challenge 3
    # api.add_resource(ViewsV2,'/')
    api.add_resource(OrderResourcesV2, '/api/v2/orders/')
    api.add_resource(OrderSpecificResourcesV2,'/api/v2/orders/<int:order_id>' )

    #register endpoiny for challenge 3 user
    api.add_resource(UserResource,'/api/v2/signup/')
    api.add_resource(GetAllUsersResources,'/api/v2/users/')
    api.add_resource(UserLogin, '/api/v2/login/')
    api.add_resource(MenuResources, '/api/v2/menu/')

    
    return app
