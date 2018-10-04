from flask import Flask
import unittest
import json
from app import create_app, connect
from .test_auth import create_admin_token

class TestDevelopmentConfig(unittest.TestCase):
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
      
        self.admin_token = create_admin_token()

    def tearDown(self):
        self.api_test_client = None
    
    def test_create_menu(self):
        """
            Test create correct menu
        """
        res = self.client.post('api/v2/menu/', data=json.dumps(self.correct_menu),content_type='application/json',  headers={'Authorization': 'Bearer ' + self.admin_token})
        self.assertIn('Description cannot be left Blank!', str(res.data))
        
    