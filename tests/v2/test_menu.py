from flask import Flask
import unittest
import json
from app import create_app, connect
from .test_auth import create_admin_token
from tests.base import BaseTestCase

class TestDevelopmentConfig(BaseTestCase):

    
    def test_create_menu(self):
        """
            Test create correct menu
        """
        res = self.client.post(
            '/api/v2/menu/',
            data=json.dumps(self.correct_menu),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + self.admin_token}
        )
        self.assertIn('Description cannot be left Blank!', str(res.data))
    
    def test_get_menu(self):
        """
            Test create correct menu
        """
        res = self.client.get(
            '/api/v2/menu/1',            
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + self.admin_token}
        )
        self.assertEqual(res.status_code, 405)
        
    