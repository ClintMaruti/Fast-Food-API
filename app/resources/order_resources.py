from flask import request, jsonify, abort, Blueprint
from flask_restful import Resource, reqparse

#import models module
from app.models import Orders

FOOD_ORDERS = Orders()

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
        return jsonify(FOOD_ORDERS.all_order())
    
    def post(self):
        """
            endpoint to Insert new list of order
        """
        parser = reqparse.RequestParser()
        order_id = 4
    
        parser.add_argument("name",type=str,required=True)
        parser.add_argument("price",type=str,required=True)
        parser.add_argument("status",type=str,required=True)
        data = parser.parse_args()
        order = {
		'id': order_id, 
        'name':data['name'],
        'price':data['price'],
		'status':data['status'] 
		}

        return jsonify(FOOD_ORDERS.insert_order(order))

class SpecificOrder(Resource):
    def get(self, order_id):
        """
        endpoint to Get a list of a specific order
        """
        if isinstance(order_id, int):
            return jsonify(FOOD_ORDERS.order_id), 200
        return jsonify({"Message":"Invalid input"}), 400
    
    def put(self, order_id):
        """
        endpoint to Update a list of a specific order
        """
        parser = reqparse.RequestParser()

        parser.add_argument("status",type=str,required=True)
        data = parser.parse_args()
        order = {
		'status':data['status'] 
		}
        if isinstance(order_id, int):
            return jsonify(FOOD_ORDERS.order_update(order_id, order))
        return jsonify({"message": "Error in the order update"})
        

    



        

