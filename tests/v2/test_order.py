from flask import Flask
import unittest
import json
from app import create_app, connect
from .test_auth import create_admin_token
from tests.base import BaseTestCase

class TestDevelopmentConfig(BaseTestCase):

    
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
    
    def test_place_order_when_price_is_below_zero(self):
        """
            Test Place an Order when price is less than zero
        """
        res = self.client.post('api/v2/orders/', data=json.dumps(self.price_below_zero),content_type='application/json')
        self.assertEqual(json.loads(res.data)["Message"], "Price must be greater than zero!")
        self.assertEqual(res.status_code, 400)

    def test_place_order_when_quantity_is_below_zero(self):
        """
            Test Place an Order when quantity is less than zero
        """
        res = self.client.post('api/v2/orders/', data=json.dumps(self.quantity_below_zero),content_type='application/json')
        self.assertEqual(json.loads(res.data)["Message"], "Quantity cannot be less than zero!")
        self.assertEqual(res.status_code, 400)

    def test_get_all_orders(self):
        """
            Test fetch all orders
        """
        res = self.client.post('api/v2/orders/', data=json.dumps(self.correct_order),content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res2 = self.client.get('api/v2/orders/', content_type='application/json', headers={'Authorization': 'Bearer ' + self.admin_token} )
        self.assertEqual(res2.status_code, 200)
    
     
