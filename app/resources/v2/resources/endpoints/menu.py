from flask import request, jsonify
from flask_restful import Resource, reqparse
from flask_httpauth import HTTPBasicAuth

#import models module
from ...models.model import FoodMenu

auth = HTTPBasicAuth()

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
        

        return jsonify({'Menu': menu_query})
    
    @auth.login_required
    def post(self):
        """Function to Add a meal option to the menu"""
        data = MenuResources.parser.parse_args()

        name = data['name']
        price = data['price']
        description = data['description']

        menu = FoodMenu(name,price,description)
        menu.insert_menu()
        response = jsonify({"Message:": "Your menu was placed successfully!"})
        response.status_code = 201
        return response
       