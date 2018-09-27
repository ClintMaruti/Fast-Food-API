import pytest
import unittest
import json
from app import create_app


class TestOrders(unittest.TestCase):

    def setUp(self):

        self.app = create_app(config_name="testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        self.sample_case_1 = 2

        self.sample_case_2 = {
            "name": "Kebab",
            "price": 500,
            "quantity": 2,    
        }

        self.sample_case_3 = {
            "name": "Kebab",
            "price": 500,
            "quantity": -2,    
        }
        self.sample_case_4 = {
            "name": "Chips",
            "price": -5,
            "quantity": 5,
        }
        self.sample_case_5 = {
            "name": "",
            "price": 500,
            "quantity": 5,
        }
        self.sample_case_6 = {
            "quantity": 2
        }

    def tearDown(self):
        self.api_test_client = None

############################## Tests for POST Endpoints ##############################
    def test_reject_order_if_name_is_empty(self): 
        """
            Test Order if name is empty
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_5), content_type='application/json')
        self.assertEqual(json.loads(res.data)["message"],"Name required. Invalid Order")
        self.assertEqual(res.status_code, 400)
    
    def test_reject_order_if_price_is_less_than_zero(self):
        """
            Test order if price is less than 0
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_4), content_type='application/json')
        self.assertEqual(json.loads(res.data)["message"],"Price must be greater than 0")
        self.assertEqual(res.status_code, 400)

    def test_reject_order_if_quanity_is_less_than_zero(self):
        """
            Test order if quantity is less than zero
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_3), content_type='application/json')
        self.assertEqual(json.loads(res.data)["message"],"Quantity Must Not Be less than 0")
        self.assertEqual(res.status_code, 400)
        
    def test_accept_order_if_everything_is_okay(self):
        """
            Test order if request is valid
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_2), content_type='application/json')
        self.assertEqual(json.loads(res.data)["Message"],"Your Order was Placed Successfully!")
        self.assertEqual(res.status_code, 201)

    def test_get_all_orders(self):
        """
            Test GET all orders
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_2), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.client.get('api/v1/orders')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Orders were successfully Retrieved', str(res.data))
    
    def test_accept_order_with_correct_id(self):
        """
            Test reject order when id is invalid
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_2), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.client.get('api/v1/orders/1')
        self.assertEqual(res.status_code, 200)
        self.assertIn('null', str(res.data))
    
    def test_api_can_update_order(self):
        """
            Test api can update an Order List
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_2), content_type='application/json')
        self.assertEqual(res.status_code, 201)
    
    def test_update_message_in_api(self):
        """
            Test api returns message when Update is successful
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_2), content_type='application/json')
        self.assertEqual(json.loads(res.data)["Message"],"Your Order was Placed Successfully!")
        self.assertEqual(res.status_code, 201)
    
    def test_reject_update_when_name_is_empty(self):
        """
            Test Api returns message Name required. Invalid Entry
        """
        res = res = self.client.post('api/v1/orders/0', data=json.dumps(self.sample_case_5), content_type='application/json')
        self.assertIn('The method is not', str(res.data))
        self.assertEqual(res.status_code, 405)
    
    def test_reject_update_when_price_is_wrong(self):
        """
            Test Api returns message Name required. Invalid Entry
        """
        res = res = self.client.post('api/v1/orders/', data=json.dumps(self.sample_case_2), content_type='application/json') 
        self.assertEqual(res.status_code, 201)
        res = res = self.client.post('api/v1/orders/0', data=json.dumps(self.sample_case_5), content_type='application/json')
        self.assertIn('The method is not', str(res.data))
        self.assertEqual(res.status_code, 405)

    def test_reject_update_when_quantiy_is_wrong(self):
        """
            Test Api returns message Name required. Invalid Entry
        """
        res = res = self.client.post('api/v1/orders/', data=json.dumps(self.sample_case_2), content_type='application/json') 
        self.assertEqual(res.status_code, 201)
        res = res = self.client.post('api/v1/orders/0', data=json.dumps(self.sample_case_3), content_type='application/json')
        self.assertIn('The method is not', str(res.data))
        self.assertEqual(res.status_code, 405)
    
if __name__ == '__main__':
    unittest.main()