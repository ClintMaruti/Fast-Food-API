from flask import request, jsonify, abort, Blueprint
from flask_restful import Resource, reqparse

#import models module
from app.models import Order,orders

#create an instance of the Class
order_list = Order()

class Views(Resource):
    def get(self):
        """
        Generate a Simple HTML home page
        """
        return '''<h1>Fast-Food-Fast APi</h1>
                    <p>A prototype API for Fast Food Fast app.</p>'''

class OrderResources(Resource):
    def get(self):
        """
        endpoint to Get a list of orders
        """
        
        if len(orders) == 0:
            response = jsonify({"message": "No Order Available"})
            response.status_code = 400
            return response
        response = jsonify ({"Orders": orders,"Message": "Orders were successfully Retrieved"})
        response.status_code = 200
        return response
            
    def post(self):
        """
            endpoint to Insert new list of order
        """
        parser = reqparse.RequestParser()
        
        data = request.get_json()

        parser.add_argument("name",type=str,required=True, help="Name cannot be blank!")
        parser.add_argument("price",type=int,required=True, help='Price Cannot be left Blank')
        parser.add_argument("quantity",type=int,required=True, help='Quantity Cannot be left Blank')

        data = parser.parse_args()

        name = data['name']
        price = data['price']
        quantity = data['quantity']
        
        if name == "":
            response = jsonify({"message": 'Name required. Invalid Order'})
            response.status_code = 400
            return response
        elif price <= 0:
            response = jsonify({"message": 'Price must be greater than 0'})
            response.status_code = 400
            return response
        elif quantity <= 0:
            response = jsonify({"message": 'Quantity Must Not Be less than 0'})
            response.status_code = 400
            return response
        else:
            order = Order(name, price, quantity)
            order.insert_order()
            response = jsonify({"Order:": order.order_payload(), "Message": "Order was placed successfully!"})
            response.status_code = 201
            return response 
            
class SpecificOrder(Resource):
    def get(self, order_id):
        """
        endpoint to Get a list of a specific order
        """
        self.order_id = order_id

        for order in orders:
            if self.order_id != order_id:
                response = jsonify({"Message": 'The Order Is Not available!'})
                response.status_code = 400 
                return response
            else:
                response = jsonify({"Orders": order, "Message": 'Your Order was retrieved Successfully'})
                response.status_code = 200
                return response
       
    def put(self, order_id):
        """
        endpoint to Update a list of a specific order
        """
        parser = reqparse.RequestParser()

        parser.add_argument("name",type=str,required=True)
        parser.add_argument("price",type=str,required=True)
        parser.add_argument("quantity",type=str,required=True)

        data = parser.parse_args()

        name = data['name']
        price = data['price']
        quantity = data['quantity']            

        if name == "":
            response = jsonify({"Message": 'Name required. Invalid Entry'})
            response.status_code = 400
            return response
        elif not price:
            response = jsonify({"Message": 'Price must be greater than 0'})
            response.status_code = 400
            return response
        elif not quantity:
            response = jsonify({"Message": 'Quantity Must Not Be less than 0'})
            response.status_code = 400
            return response
        else:
            order_update = order_list.order_update(order_id,name,price,quantity)
            response = jsonify({"Orders": order_update,"Message": 'Your Order was Updated Successfully!'})
            response.status_code = 200
            return response 
