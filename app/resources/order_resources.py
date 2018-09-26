from flask import request, jsonify, abort, Blueprint
from flask_restful import Resource, reqparse

#import models module
from app.models import Orders

#creat an instance of the Class
bucket1 = Orders()

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
        bucketall = bucket1.all_order()
        return bucketall
        
    def post(self):
        """
            endpoint to Insert new list of order
        """
        data = request.get_json()
        name = data['name']
        price = data['price']
        quantity = data['quantity']
        res = bucket1.insert_order(name,price,quantity)
        return res

class SpecificOrder(Resource):
    def get(self, order_id):
        """
        endpoint to Get a list of a specific order
        """
        if isinstance(order_id, int):
            bucket = bucket1.all_order()
            return bucket
        return jsonify({"Message":"Invalid input"})

    def put(self, order_id):
        """
        endpoint to Update a list of a specific order
        """
        parser = reqparse.RequestParser()

        parser.add_argument("name",type=str,required=True)
        parser.add_argument("price",type=str,required=True)
        parser.add_argument("quan0tity",type=str,required=True)
        data = parser.parse_args()
        name = data['name']
        price = data['name']
        quantity = data['quantity']

        order = {
		'name':data['name'] 
		}

        bucketupdate = bucket1.order_update(order_id,name,price,quantity)
        if isinstance(order_id, int):
            return bucketupdate
        return jsonify({"message": "Error in the order update"})
