from flask import request, jsonify
from flask_restful import Resource, reqparse

#import models module
from ...models.model import Order


class ViewsV2(Resource):
    def get(self):
        """
            Generate a simple HTML home page
        """
        return '''<h1>Fast-Food-Fast APi</h1>
                    <p>A prototype API for Fast Food Fast app.</p>'''
    
class OrderResourcesV2(Resource):
    """Flask restful class that hold the routes function for the Menu Endpoints"""
    parser = reqparse.RequestParser()

    parser.add_argument("name",type=str,required=True, help="Name cannot be blank!")
    parser.add_argument("price",type=int,required=True, help='Price cannot be below zero')
    parser.add_argument("quantity",type=int,required=True, help="Quantity cannot be below zero")


    def post(self):
        """
            Endpoint to place an order for food
        """
        data = OrderResourcesV2.parser.parse_args()

        name = data['name']
        price = data['price']
        quantity = data['quantity']

        # #inisialize User class from Models
        # orderObject = Order()

        # if name == "":
        #     response = jsonify({"Message": 'Name required. Invalid Order!'})
        #     response.status_code = 400
        #     return response

        # elif price <= 0:
        #     response = jsonify({"Message": "Price must be greater than zero!"})
        #     response.status_code = 400
        #     return response

        # elif quantity <= 0:
        #     response = jsonify({"Message": "Quantity cannot be less than zero!"})
        #     response.status_code = 400
        #     return response

        # else:
        #     #Instanciate the class
        #     orderObject = Order(name,price,quantity)

        #     orderObject.place_order()

        #     response = jsonify({"Message: ": "Your Order was placed successfully!"})
        #     response.status_code = 201
        #     return response

        order = Order(name,price,quantity)
        order.place_order()
        response = jsonify({"Message:": "Your Order was placed successfully!"})
        response.status_code = 201
        return response

    def get(self):
        """
            Endpoint to fetch all order for food
        """
        #instanciate class
        orderObject = Order()
        order_query = orderObject.all_order()
        return order_query
