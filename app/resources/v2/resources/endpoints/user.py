from flask import request, jsonify, json, abort, make_response
from passlib.apps import custom_app_context as pwd_context
from flask_restful import Resource, reqparse
from flask_httpauth import HTTPBasicAuth
from datetime import datetime, timedelta
import jwt
import os
from functools import wraps

#import models module
from ...models.model import User
from app.resources.v2.resources.endpoints.auth import token_required , key, wraps
key = os.getenv('SECRET_KEY')

# def token_required(function):
#     @wraps(function)
#     def decorated(*args, **kwargs):
#         token = request.args.get('token')
#         if not token:
#             return jsonify({'message' : 'Token is requied'})

#         try:
#             data = jwt.decode(token, key)
#         except:
#             return jsonify({'Message: ': 'Token is invalid!'})

#         return function(*args, **kwargs)
#     return decorated

class UserResource(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("name",type=str,required=True, help="Name cannot be blank!")
    parser.add_argument("email", type=str, required=True, help="Email required!")
    parser.add_argument("admin", type=bool, required=True, help="Role cannot be left blank")
    parser.add_argument("password", type=str, required=True, help="Password canot be left blank")


    def post(self):
        """
            This function adds a user into the database and assigns them a role
        """
        data = UserResource.parser.parse_args()

        username = data['name']
        email = data['email']
        admin = data['admin']
        password = data['password']

        userObject = User(username,password)

        if userObject.getusername(username) == False:
            response = jsonify({'message': 'The User you requested already exists!'})
            response.status_code = 400
            return response


        hashed_password = userObject.hash_password(password)

        userObject = User(username,email,hashed_password,admin)
        userObject.addUser()
        return ({"Message: ": "User added successfuly!"})

class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name",type=str,required=True, help="Name cannot be blank!")
    parser.add_argument("password", type=str, required=True, help="You haven't entered your password!")

    
    def post(self):
        """
            This function let's a user login into the app
        """
        data = UserLogin.parser.parse_args()

        username = data['name']
        password = data['password']
 
        #initialize User class from Models
        userObject = User(username,password)
        print (userObject)
        response = userObject.login()
        if response == True:
            token = jwt.encode({'user':username, 'exp': datetime.utcnow() + timedelta(minutes=30)},key)  
            res = "Login Successful!"
            message = str(token)
        return jsonify({"Message: ":res, "Token: ": message})
        

class GetAllUsersResources(Resource):
    """
        This function is responsibe to Get all Users Registered
    """
    @token_required
    def get(self):
        """
            This function fetchs all users from the database and returns
        """
        userObject = User(name=None,password=None)
        json_data = userObject.getallUser()

        return json_data