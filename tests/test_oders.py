import pytest
import json
from app import create_app

app = create_app(config_name="TESTING")
client = app.test_client()

################# Tests for GET endpoints ##################

def test_all_orders():
    """
        Test for GET all orders
    """
    res = client.get('api/v1/orders')
    assert res.status_code == 200

def test_get_specific_order():
    """
        Test for GET specific orders
    """
    res = client.get('api/v1/orders/0')
    assert res.status_code == 200

def test_invalid_user_get_responce():
    """
        Test for if user request for order using String
    """
    res = client.get('api/v1/orders/cli')
    assert res.status_code == 404
    
    