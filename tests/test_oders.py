import pytest
import json
from app import create_app

app = create_app(config_name="TESTING")
client = app.test_client()

order_correct = {

    "name": "Urban Burger",
    "price": 800,
    "status": "Delivered"
}
order_less_name = {
    "id": 1,
    "price": 800,
    "status": "Delivered"
}

order_less_price = {
    "id": 1,
    "name": "Kebab",
    "status": "Delivered"
}

nill_order = {}


############################## Tests for POST Endpoints ##############################
def test_nill_order(): 
    """
        Test empty order
    """
    res = client.post('api/v1/orders', data=nill_order)
    assert res.status_code == 400

def test_order_without_name():
    """
        Test order without name
    """
    res = client.post('api/v1/orders', data = order_less_name)
    assert res.status_code == 400

def test_order_without_price():
    """
        Test order without price   
    """
    res = client.post('api/v1/orders', data= order_less_price)
    assert res.status_code == 400
    
def test_order_add_all():
    """
        Test to add correct order, excluding id number since it is automatically incremented
    """
    res = client.post('api/v1/orders', data=order_correct)
    assert res.status_code == 201

############################## Tests for GET Endpoints ##############################
    
def test_all_orders():
    """
        Test for GET all orders
    """
    res = client.get('api/v1/orders')
    assert res.status_code == 200





