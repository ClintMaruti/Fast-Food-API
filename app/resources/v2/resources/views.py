from flask import request, jsonify
from flask_restful import Resource, reqparse

#import models module
from ..models.model import Order 

#instanciate class
menu = Order()


class Views(Resource):
    def get(self):
        """
            Generate a simple HTML home page
        """
        return '''<h1>Fast-Food-Fast APi</h1>
                    <p>A prototype API for Fast Food Fast app.</p>'''
    
class OrderResources(Resource):
    def get(self):
        """
            Endpoint to Get menu
        """
        if menu.all_order() is None:
            response = jsonify({"Message: ": "No order available!"})
            response.status_code = 400
            return response
        return menu.all_order()
    
    def post(self):
        """
            Endpoint to add food option to menu
        """
        parser = reqparse.RequestParser()

        data = request.get_json()

        parser.add_argument("name",type=str,required=True, help="Name cannot be blank!")
        parser.add_argument("price",type=int,required=True, help='Rate cannot be converted')
        parser.add_argument("quantity",type=int,required=True)

        name = data['name']
        price = data['price']
        quantity = data['quantity']

        if name == "":
            response = jsonify({"Message": 'Name required. Invalid Order!'})
            response.status_code = 400
            return response
        elif price <= 0:
            response = jsonify({"Message": "Price must be greater than zero!"})
            response.status_code = 400
            return response
        elif quantity <= 0:
            response = jsonify({"Message": "Quantity cannot be less than zero!"})
            response.status_code = 400
            return response
        else:
            response = jsonify({"Message": "Your Order was placed successfully!"})
            response.status_code = 201
            return jsonify({"Your Order: ": menu.insert_order, "Message": response})
    

        
    


