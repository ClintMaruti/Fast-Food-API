from flask import Flask
import unittest
import json
from app import create_app, connect

class TestDevelopmentConfig(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        self.correct_order = {
            "name": "itemtwo",
            "price": 800,
            "quantity": 5,
            "status" : "Delivered"
        }
        self.name_missing = {
            "name": "",
            "price": 800,
            "quantity": 5,
            "status" : "Delivered"
        }
    def tearDown(self):
        self.api_test_client = None
    
    def test_place_order_into_db(self):
        """
            Test place order when everything is okay
        """
        res = self.client.post('api/v2/orders/', data=json.dumps(self.correct_order),content_type='application/json')
        self.assertEqual(json.loads(res.data)["Message: "],"Your Order was placed successfully!")
    
    def test_place_order_with_missing_name(self):
        """
            Test place an order with a missing name
        """
        res = self.client.post('api/v2/orders/', data=json.dumps(self.name_missing),content_type='application/json')
        self.assertEqual(json.loads(res.data)["Message"],"Name required. Invalid Order!")
