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
    
    def test_create_menu_with_empty_name(self):
        """
            Test create correct menu with Empty name
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
            Test fetch the menu items
        """
        res = self.client.get(
            '/api/v2/menu/',            
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + self.admin_token}
        )
        self.assertEqual(res.status_code, 200)
        
    
    def test_delete_menu(self):
        """
            Test delete menu
        """
        res = self.client.delete(
            '/api/v2/menu/1',            
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + self.admin_token}
        )
        self.assertEqual(res.status_code, 200)
    
    def test_menu_with_invalid_price(self):
        """
            Test menu with an invalif price
        """
        res = self.client.post(
            '/api/v2/menu/',
            data=json.dumps(self.menu_with_invalid_price),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + self.admin_token}
        )
        self.assertIn('Price must be greater than zero!', str(res.data))
        self.assertEqual(res.status_code, 400)
    
    def test_menu_with_invalid_description(self):
        """
            Test create correct menu
        """
        res = self.client.post(
            '/api/v2/menu/',
            data=json.dumps(self.menu_with_invalid_description)
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + self.admin_token}
        )
        self.assertIn('Description must not be left Blank', str(res.data))
        self.assertEqual(res.status_code, 400)
        
        
    