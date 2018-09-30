from flask import request, jsonify, json, abort
from flask_restful import Resource, reqparse

#import models module
from ...models.model import User



class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name",type=str,required=True, help="Name cannot be blank!")
    parser.add_argument("email", type=str, required=True, help="Email required!")
    parser.add_argument("admin", type=bool, required=True, help="Role cannot be left blank")
    parser.add_argument("token", type=str, required=True, help="Token cannot be left blank")
    parser.add_argument("password", type=str, required=True, help="Password canot be left blank")

    def get(self):
        """
            This function fetchs all users from the database and returns
        """
        userObject = User()
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
        token = data['token']
        password = data['password']

        userObject = User()

        if userObject.getusername(username):
            response = jsonify({'message': 'The User you requested already exists!'})
            response.status_code = 400
            return response


        hashed_password = userObject.hash_password(password)
        token = '46465465'

        userObject = User(username,email,hashed_password,admin,token)
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

        #inisialize User class from Models
        userObject = User()

        hashed_password = hashed_password = userObject.hash_password(password)
        
        if username is not userObject.getusername or hashed_password is not userObject.getpasword:
            response = jsonify({"Message: ": "Login Failed, Check your username or password!"})
            response.status_code = 403
            return response
        return jsonify({"Message: ": "Login Successful!"})
        


        


