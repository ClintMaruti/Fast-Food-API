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
    
    def post(self):
        """
            endpoint to Insert new list of order
        """
        if not request.json or not 'name' in request.json:
            abort(400)
            order = {
                'id': orders[-1]['id'] + 1,
                'name': request.json['name'],
                'price': request.json['price'],
                'status': request.json['status'],
                    }
        orders.append(order)
        return jsonify({'order': order}), 201

class SpecificOrder(Resource):
    def get(self, order_id):
        """
        endpoint to Get a list of a specific order
        """
        order = [order for order in orders if order['id'] == order_id]
        if len(order) == 0:
            return "Error: Id not found"
        return jsonify({'order': order[0]})
    
    def put(self, order_id):
        """
        endpoint to Update a list of a specific order
        """
        order = [order for order in orders if order['id'] == order_id]
        if len(order) == 0:
            abort(404)
            if not request.json:               
                abort(400)
            if 'name' in request.json and not isinstance(request.json['name'], str):
                abort(400)
            if 'price' in request.json and not isinstance(request.json['price'], str):
                abort(400)
            if 'status' in request.json and not isinstance(request.json['status'], bool):
                abort(400)
        order[0]['name'] = request.json.get('name', order[0]['name'])
        order[0]['price'] = request.json.get('price', order[0]['price'])
        order[0]['status'] = request.json.get('status', order[0]['status'])
        return jsonify({'order': order[0]})
    



        


