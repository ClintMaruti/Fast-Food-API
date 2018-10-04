from flask import request, jsonify
from flask_restful import Resource, reqparse
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (jwt_required, get_jwt_identity, create_access_token)

#import models module
from ...models.model import Order
from app.resources.v2.resources.endpoints.auth import token_required , key, wraps

auth = HTTPBasicAuth()
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
    parser.add_argument("status",type=str,required=True, help='status must be included')
    parser.add_argument("quantity",type=int,required=True, help="Quantity cannot be below zero")


    def post(self):
        """
            Endpoint to place an order for food
        """
        data = OrderResourcesV2.parser.parse_args()

        name = data['name']
        price = data['price']
        status = data['status']
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
            #Instanciate the class
            orderObject = Order(name,price,quantity,status)
            orderObject.place_order()
            response = jsonify({"Message: ": "Your Order was placed successfully!"})
            response.status_code = 201
            return response

    @jwt_required
    def get(self):
        """
            Endpoint to fetch all order for food
        """
        #instanciate class
        orderObject = Order()
        order_query = orderObject.all_order()
        order_list = []
        if order_query:
            for order in order_query:
                collect = {
                    "Order_ID": order[0],
                    "Name of Food": order[1],
                    "Price": order[2],
                    "Quantity": order[3],
                    "Status": order[4],
                  
                                    }
                order_list.append(collect)
        return order_list

class OrderSpecificResourcesV2(Resource):
    """
        Class that holds endpoints to get single order and update single order
    """
    parser = reqparse.RequestParser()

    parser.add_argument("status",type=str,required=True, help='status must be included')
    
    @jwt_required
    def get(self, order_id):
        """
            Endpoint to Get a specific list of order
        """
        orderObject = Order()
        result = orderObject.order_id(order_id)
        return result
        
    @jwt_required
    def post(self, order_id):
        """
            Endpoint to Update order status
        """
        data = OrderSpecificResourcesV2.parser.parse_args()

        status = data['status']

        orderObject = Order()
        response = jsonify({"Message: ": "Orders Updated Successfully"})
        response.status_code = 201
        return response
