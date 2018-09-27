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

        self.sample_case_quantity_invalid = {
            "name": "Kebab",
            "price": 500,
            "quantity": -2,    
        }
        self.sample_case_price_invalid = {
            "name": "Chips",
            "price": -5,
            "quantity": 5,
        }
        self.sample_case_name_empty = {
            "name": "",
            "price": 500,
            "quantity": 5,
        }
        self.sample_case_6 = {
            "quantity": 2
        }

    def tearDown(self):
        self.api_test_client = None

        
    def test_accept_order_if_order_is_okay(self):
        """
            Test order if request is valid
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_2), content_type='application/json')
        self.assertEqual(json.loads(res.data)["Message"],"Order was placed successfully!")
        self.assertEqual(res.status_code, 201)
    
    def test_order_message_when_name_the_is_empty(self):
        """
            Test returns message if name is missing
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_name_empty), content_type='application/json')
        self.assertEqual(json.loads(res.data)["message"],"Name required. Invalid Order")
    
    def test_order_message_when_the_price_is_less_than_zero(self):
        """
            Test returns message if price is less than zero
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_price_invalid), content_type='application/json')
        self.assertEqual(json.loads(res.data)["message"], "Price must be greater than 0")
    
    def test_order_message_when_quantity_is_less_than_zero(self):
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_quantity_invalid), content_type='application/json')
        self.assertEqual(json.loads(res.data)["message"], "Quantity Must Not Be less than 0")
    
    def test_succesful_insert_order(self):
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_2), content_type='application/json')
        self.assertEqual(json.loads(res.data)["Message"], "Order was placed successfully!")

    def test_post_message_if_name_is_empty(self):
        """
            Test Post if name is empty
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_quantity_invalid), content_type='application/json')
        self.assertEqual(json.loads(res.data)["message"],"Quantity Must Not Be less than 0")
    
    def test_get_single_order(self):
        """
            Test Get for single order
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_2), content_type='application/json') 
        self.assertEqual(json.loads(res.data)["Message"], "Order was placed successfully!")

        #Get List
        get_order = self.client.get('api/v1/orders/1')
        self.assertEqual(get_order.status_code, 200)
        self.assertEqual(json.loads(get_order.data)["Message"],'Your Order was retrieved Successfully')
    
    def test_get_order_which_is_unavailable(self):
        """
            Test Get for unavailable
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_2), content_type='application/json') 
        self.assertEqual(json.loads(res.data)["Message"], "Order was placed successfully!")

        #Get List
        get_order = self.client.get('api/v1/orders/8')
        self.assertEqual(get_order.status_code, 400)
        self.assertEqual(json.loads(get_order.data)["Message"],'The Order Is Not available!')

    
    def test_reject_update_if_name_is_empty(self):
        """
            Test Api returns message Name required. Invalid Entry
        """
        res = self.client.post('api/v1/orders/', data=json.dumps(self.sample_case_2), content_type='application/json')
        self.assertEqual(json.loads(res.data)["Message"], "Order was placed successfully!" )
        self.assertEqual(res.status_code, 201)
        #update
        update_res = self.client.put('api/v1/orders/1', data=json.dumps(self.sample_case_name_empty), content_type='application/json')
        self.assertEqual(json.loads(update_res.data)["Message"],"Name required. Invalid Entry")
        self.assertEqual(update_res.status_code, 400)
    
    def test_all_order_returns(self):
        """
            Test All order returns
        """
        res = self.client.post('api/v1/orders', data=json.dumps(self.sample_case_2), content_type='application/json') 
        self.assertEqual(json.loads(res.data)["Message"], "Order was placed successfully!")

        #Get List
        get_order = self.client.get('api/v1/orders/')
        self.assertEqual(get_order.status_code, 200)
        self.assertEqual(json.loads(get_order.data)["Message"],"Orders were successfully Retrieved")
        
    


    
if __name__ == '__main__':
    unittest.main()
    