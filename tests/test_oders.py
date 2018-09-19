import pytest
import json
from app import create_app

app = create_app(config_name="TESTING")
client = app.test_client()

######################### Tests for Put Order ######################
order = { "status": "pending"}

def test_for_update_order():
    """
        Test for PUT endpoint to update order
    """
    res = client.put('api/v1/orders/0', data = order)
    assert res.status_code == 404
