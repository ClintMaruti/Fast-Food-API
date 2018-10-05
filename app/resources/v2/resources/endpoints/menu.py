from flask import request, jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import (jwt_required, get_jwt_identity, create_access_token)

#import models module
from ...models.model import FoodMenu


class MenuResources(Resource):
    """Flask restful class that hold the routes function for the Menu Endpoints"""
    parser = reqparse.RequestParser()

    parser.add_argument("name",type=str,required=True, help="Name cannot be blank!")
    parser.add_argument("price",type=int,required=True, help='Price cannot be below zero')
    parser.add_argument("description",type=str,required=True, help="Description cannot be left Blank!")

    def get(self):
        """Function that returns the menu to the user"""

        menuObject = FoodMenu()
        menu_query = menuObject.get_menu()
        serialized = []
        if menu_query:
            for item in menu_query:
                collect = {
                    "Menu_ID" : item[0],
                    "Prices": item[1],
                    "Description": item[2],
                       }
                serialized.append(collect) 
            return jsonify({'Menu': serialized})
        
    @jwt_required
    def post(self):
        """Function to Add a meal option to the menu"""
        data = MenuResources.parser.parse_args()

        name = data['name']
        price = data['price']
        description = data['description']

        if name == "":
            response = jsonify({"Message": 'Name of food required. Invalid Order!'})
            response.status_code = 400
            return response

        elif price <= 0:
            response = jsonify({"Message": "Price must be greater than zero!"})
            response.status_code = 400
            return response
        
        elif description == "":
            response = jsonify({"Message": "Description must not be left Blank"})
            response.status_code = 400
            return response

        else:
            menu = FoodMenu(name,price,description)
            menu.insert_menu()
            response = jsonify({"Message:": "Your menu was placed successfully!"})
            response.status_code = 201
            return response
            
class DeleteMenu(Resource):
    """
        This class model holds the the function to delte a specific user by Id
    """
    @jwt_required
    def delete(self,id):
        """
            This function deletes a user from the database
        """
        menuObject = FoodMenu()
        result = menuObject.delete(id)
        return result
