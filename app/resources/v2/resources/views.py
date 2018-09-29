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
            Endpoint to Get a list of orders
        """
        if menu.all_order() is None:
            response = jsonify({"Message: ": "No order available!"})
            response.status_code = 400
            return response
        return menu.all_order()



