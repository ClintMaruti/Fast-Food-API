from flask import request, jsonify, abort, Blueprint
from flask_restful import Resource

#import models module
from app.models import orders


class OrderResources(Resource):
    def get(self):
        """
        endpoint to Get a list of orders
        """
        return jsonify(orders)

class SpecificOrder(Resource):
    def get(self, order_id):
        """
        endpoint to Get a list of a specific order
        """
        order = [order for order in orders if order['id'] == order_id]
        if len(order) == 0:
            return "Error: Id not found"
        return jsonify({'order': order[0]})
    



        


