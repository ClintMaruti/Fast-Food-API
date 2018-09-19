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
    



        


