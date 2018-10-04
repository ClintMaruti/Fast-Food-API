from flask import Flask
import unittest
import json
from app import create_app, connect
from tests.v2.test_auth import create_admin_token


class BaseTestCase(unittest.TestCase):
    """ Base Tests """
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        self.correct_menu = {
            "name": "Burger Tuple",
            "price": 800,
            "decription": "This is a burger Tuples"
            }
        self.correct_order = {
            "userID":3,
            "name": "itemtwo",
            "price": 800,
            "quantity": 5,
            "status" : "Delivered"
        }
        self.name_missing = {
            "userID":3,
            "name": "",
            "price": 800,
            "quantity": 5,
            "status" : "Delivered"
        }
        self.price_below_zero = {
            "userID":3,
            "name": "Chicken Tikka",
            "price": -4,
            "quantity": 5,
            "status" : "Delivered"
        }
        self.quantity_below_zero = {
            "userID":3,
            "name": "Chicken Tikka",
            "price": 800,
            "quantity": -5,
            "status" : "Delivered"
        }
        self.menu_with_invalid_price= {
            "name":"Chicken Tikka",
            "price":-8,
            "description":"This is the desription"                                     
        }
        
        self.menu_with_invalid_description= {
            "name":"Chicken Tikka",
            "price":500,
            "description":""                                     
        }      
        self.admin_token = create_admin_token()

    def tearDown(self):
        self.api_test_client = None
