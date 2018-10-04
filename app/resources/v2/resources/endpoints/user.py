from flask import request, jsonify, json, abort, make_response
from passlib.apps import custom_app_context as pwd_context
from flask_restful import Resource, reqparse
from flask_httpauth import HTTPBasicAuth
from datetime import datetime, timedelta
import jwt
from flask_jwt_extended import (jwt_required, get_jwt_identity, create_access_token)

import os
from functools import wraps

#import models module
from ...models.model import User
from app.resources.v2.resources.endpoints.auth import token_required , key, wraps
from app.resources.v2.resources.endpoints.validate import passwd_check
key = os.getenv('SECRET_KEY')


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

        if passwd_check(password) == False:
            response = jsonify({"message": "The password length must be greater than 6 and less than 8, has at least one uppercase letter,  has at least one lowercase letter, has at least one numeral, has any of the required special symbols"})
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
        response = userObject.login()
        if response == True:
            # token = jwt.encode({'user':username, 'exp': datetime.utcnow() + timedelta(minutes=30)},key)
            expires = timedelta(minutes=30)  
            token = create_access_token(identity=username, expires_delta=expires)
            res = "Login Successful!"
            message = str(token)
            return jsonify({"Message: ":res, "Token: ": message})
        return jsonify({"Message": "Invalid Login"})

class GetAllUsersResources(Resource):
    """
        This function is responsibe to Get all Users Registered
    """
    @jwt_required
    def get(self):
        """
            This function fetchs all users from the database and returns
        """
        userObject = User(name=None,password=None)
        json_data = userObject.getallUser()
        user_lit = []
        if json_data:
            for data in json_data:
                collect = {
                    "User_id" : data[0],
                    "User Name": data[1],
                    "Email": data[2],
                    "Password": data[3],
                    "Admin": data[4]
                }
                user_lit.append(collect)               
        return user_lit

class DeleteUser(Resource):
    """
        This class model holds the the function to delte a specific user by Id

    """
    @jwt_required
    def delete(self,id):
        """
            This function deletes a user from the database
        """
        userObject = User(name=None,password=None)
        result = userObject.delete(id)
        return result
