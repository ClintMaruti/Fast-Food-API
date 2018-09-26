import pytest
import unittest
import json
from app import create_app


class TestOrders(unittest.TestCase):

    def setUp(self):

        self.app = create_app(config_name="TESTING")
        self.client = self.app.test_client()

        self.sample_case_1 = {
            "name": "Urban Burger",
            "price": 800,
            "quantity": "5"
                      }
        self.sample_case_2 = {
            "id": 1,
            "price": 800,
            "quantity": "7"
        }
        self.sample_case_3 = {
            "id": 1,
            "name": "Kebab",
            "quantity": "8"    
        }
        self.sample_case_4 = {
            "quantity": "7"
        }
        self.sample_case_5 = {

        }
        self.sample_case_6 = {
            "quantity": 2
        }

    def tearDown(self):
        self.api_test_client = None

############################## Tests for POST Endpoints ##############################
    def test_nill_order(self): 
        """
            Test empty order
        """
        self.res = self.client.post('api/v1/orders', data= self.sample_case_5)
        assert self.res.status_code == 500

    def test_order_without_name(self):
        """
        Test order without name
        """
        self.res = self.client.post('api/v1/orders', data = self.sample_case_2)
        assert self.res.status_code == 500

    def test_order_without_price(self):
        """
            Test order without price   
        """
        self.res = self.client.post('api/v1/orders', data= self.sample_case_3)
        assert self.res.status_code == 500
    
    def test_order_add_all(self):
        """
            Test to add correct order, excluding id number since it is automatically incremented
        """
        self.res = self.client.post('api/v1/orders', data=self.sample_case_1)
        assert self.res.status_code == 500


############################## Tests for GET Endpoints ##############################
    
    def test_all_orders(self):
        """
            Test for GET all orders
        """
        self.res = self.client.get('api/v1/orders')
        assert self.res.status_code == 200
        self.assertIn('No Food Available', str(self.res.data))

    def test_all_orders_with_invalide_uri(self):
        """
            Test for GET all orders with invalid sequence
        """
        self.res = self.client.get('api/v1/orders7')
        assert self.res.status_code == 404

    def test_fethc_all_orders(self):
        """
            Test for GET all orders with an invalid route
        """
        self.res = self.client.get('api/v1/orderss')
        assert self.res.status_code == 404

############################## Tests for PUT Endpoints ###################################
    def test_udate_orders(self):
        """
            Test endpoint to update order when the URI is invalid
        """
        self.res = self.client.post('api/v1/orders/0') 
        assert self.res.status_code == 405

    def test_update_orders_with_bad_uri(self):
        """
            Test endpoint to update order when the URI is wrong
        """
        self.res = self.client.post('api/v1/orders/<int: order_id>') 
        assert self.res.status_code == 404

    def test_update_order_with_invalid_put(self):
        """
            Test endpoint to update order when input is wrong
        """
        self.res = self.client.post('api/v1/orders/0', data= self.sample_case_3) 
        assert self.res.status_code == 405

    def test_update_order_with_empty(self):
        """
             Test endpoint to update order when input is wrong
        """
        self.res = self.client.post('api/v1/orders/0', data=self.sample_case_5) 
        assert self.res.status_code == 405

    def test_update_order_with_integ(self):
        """
            Test endpoint to update order when input is wrong
        """
        self.res = self.client.post('api/v1/orders/0', data=self.sample_case_6) 
        assert self.res.status_code == 405

if __name__ == '__main__':
    unittest.main()