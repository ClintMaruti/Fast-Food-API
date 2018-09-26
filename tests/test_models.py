import unittest
from app.models import Orders
from app import create_app

FOOD_ORDER = Orders()


class TestOrdersModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="TESTING")
        self.client = self.app.test_client()
        self.bad_order = 12
        self.sample_order = FOOD_ORDER
        

    
    def test_message_order(self):
        """ Assert That The models returns a message"""
        self.assertIn("No Food Available.", str(FOOD_ORDER.all_order()))
    




if __name__ == '__main__':
    unittest.main()