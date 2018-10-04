from flask import Flask
from flask_restful import Api

#local imports
from config import app_config
from db import connect
import os
from flask_jwt_extended import JWTManager


#challenge 3 imports
from app.resources.v2.resources.endpoints.orders import OrderResourcesV2
from app.resources.v2.resources.endpoints.orders import OrderSpecificResourcesV2
from app.resources.v2.resources.endpoints.orders import UserOrder
from app.resources.v2.resources.endpoints.user import User
from app.resources.v2.resources.endpoints.user import UserResource
from app.resources.v2.resources.endpoints.user import UserLogin
from app.resources.v2.resources.endpoints.user import DeleteUser
from app.resources.v2.resources.endpoints.menu import MenuResources
from app.resources.v2.resources.endpoints.menu import DeleteMenu
from app.resources.v2.resources.endpoints.user import GetAllUsersResources



def create_app(config_name):
    '''Function that creates flask app depending on the configuration passed'''
    
    #initialize flask app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config)
    
    jwt=JWTManager(app)
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

    #initialize api 
    api = Api(app)

    app.url_map.strict_slashes = False
 
    connect()

    api.add_resource(OrderResourcesV2, '/api/v2/orders/')
    api.add_resource(OrderSpecificResourcesV2,'/api/v2/orders/<int:order_id>' )
    api.add_resource(UserOrder,'/api/v2/orders/history/<int:user_id>' )

    #register endpoiny for challenge 3 user
    api.add_resource(UserResource,'/api/v2/signup/')
    api.add_resource(GetAllUsersResources,'/api/v2/users/')
    api.add_resource(DeleteUser, '/api/v2/users/<int:id>')
    api.add_resource(UserLogin, '/api/v2/login/')
    api.add_resource(MenuResources, '/api/v2/menu/')
    api.add_resource(DeleteMenu, '/api/v2/menu/<int:id>')
    

    
    return app
