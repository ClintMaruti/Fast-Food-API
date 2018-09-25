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

order_update_less = {
    "status": "dekakkb"
}

nill_order = {}

inte_order = {
    "status": 4
}


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
    assert res.status_code == 200
    


############################## Tests for GET Endpoints ##############################
    
def test_all_orders():
    """
        Test for GET all orders
    """
    res = client.get('api/v1/orders')
    assert res.status_code == 200

def test_all_orders_with_invalide_uri():
    """
        Test for GET all orders with invalid sequence
    """
    res = client.get('api/v1/orders7')
    assert res.status_code == 404

def test_fethc_all_orders():
    """
        Test for GET all orders with an invalid route
    """
    res = client.get('api/v1/orderss')
    assert res.status_code == 404

############################## Tests for PUT Endpoints ###################################
def test_udate_orders():
    """
        Test endpoint to update order when the URI is invalid
    """
    res = client.post('api/v1/orders/0') 
    assert res.status_code == 405

def test_update_orders_with_bad_uri():
    """
        Test endpoint to update order when the URI is wrong
    """
    res = client.post('api/v1/orders/<int: order_id>') 
    assert res.status_code == 404

def test_update_order_with_invalid_put():
    """
        Test endpoint to update order when input is wrong
    """
    res = client.post('api/v1/orders/0', data=order_update_less) 
    assert res.status_code == 405

def test_update_order_with_empty():
    """
        Test endpoint to update order when input is wrong
    """
    res = client.post('api/v1/orders/0', data=nill_order) 
    assert res.status_code == 405

def test_update_order_with_integ():
    """
        Test endpoint to update order when input is wrong
    """
    res = client.post('api/v1/orders/0', data=inte_order) 
    assert res.status_code == 405
