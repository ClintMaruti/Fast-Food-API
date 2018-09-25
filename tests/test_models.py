import unittest
from app.models import Orders
from app import create_app

FOOD_ORDER = Orders('Beef','850','5')


class TestOrdersModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="TESTING")
        self.client = self.app.test_client()
        self.bad_order = 12
        self.sample_order = FOOD_ORDER
        

    def test_order_is_list(self):
        """ Assert That The models data is a List"""
        self.assertIsInstance(FOOD_ORDER.all_order(), dict)
    
    def test_message_order(self):
        """ Assert That The models returns a message"""
        self.assertIn("No Food Available", str(FOOD_ORDER.all_order()))
    
    def test_message_in_insert(self):
        self.full_order = FOOD_ORDER.all_order()
        self.assertIn("Order Rejected", str(FOOD_ORDER.insert_order(self.sample_order)))
    
    def test_error_message_in_insert(self):
        self.assertIn("Rejected", str(FOOD_ORDER.insert_order(self.bad_order)))
    
    def test_order_id_model(self):
        self.assertIsInstance(FOOD_ORDER.order_id(0), dict)
    
    def test_order_update_model(self):
        self.assertIn("There has been", str(FOOD_ORDER.order_update(0, self.bad_order)))


if __name__ == '__main__':
    unittest.main()