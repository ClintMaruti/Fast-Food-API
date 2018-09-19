import pytest
import json
from app import create_app

app = create_app(config_name="TESTING")
client = app.test_client()

def test_all_orders():
    """
        Test for GET all orders
    """
    res = client.get('api/v1/orders')
    assert res.status_code == 200