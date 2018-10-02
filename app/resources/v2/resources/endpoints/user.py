from flask import request, jsonify, json, abort, make_response
from passlib.apps import custom_app_context as pwd_context
from flask_restful import Resource, reqparse
from flask_httpauth import HTTPBasicAuth
from datetime import datetime
from flask_jwt_extended import create_access_token

#import models module
from ...models.model import User


auth = HTTPBasicAuth()

class UserResource(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("name",type=str,required=True, help="Name cannot be blank!")
    parser.add_argument("email", type=str, required=True, help="Email required!")
    parser.add_argument("admin", type=bool, required=True, help="Role cannot be left blank")
    parser.add_argument("password", type=str, required=True, help="Password canot be left blank")

    def get(self):
        """
            This function fetchs all users from the database and returns
        """
        userObject = User(name=None,password=None)
        json_data = userObject.getallUser()

        return json_data

 
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
        userObject = User(password,username)
        response = userObject.login()
        token = userObject.generate_auth_token()
        return jsonify ({"Token":token.decode('UTF-8')})