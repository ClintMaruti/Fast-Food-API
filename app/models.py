import datetime
from flask import jsonify, sessions


class Orders(object):
  """ This class defines the Order Models"""
  def __init__(self, name=None, price=None, quantity=None):
    """ A method constructor to define Order""" 
    self.id = len(orders) + 1
    self.name = name
    self.price = price
    self.quantity = quantity
    
  def all_order(self):
    """ Model function that Fetchs all orders """
    if orders == []:
      return orders

  def insert_order(self, name, price, quantity):
    """ Model function to Insert a new Order int list """
    self.bucketlist = {}

    self.bucketlist['name'] = name
    self.bucketlist['price'] = price
    self.bucketlist['quantity'] = quantity
    self.bucketlist['order_id'] = self.id
    orders.append(self.bucketlist)
    return orders[-1]
  
  def order_id(self, order_id):
    """ Model function to GET a specific order list """
    if isinstance(order_id, int):
      for order in orders:
        if order['order_id'] == id:
          return order 
  
  def order_update(self, order_id,name,price,quantity):
    """ Model function to Update a specific order list """
    if isinstance(order_id, int):
      for order in orders:
        if order['order_id'] == id:
          order['name'] == name
          order['price'] == price
          order['quantity'] == quantity
          return orders

#sample data for test case
orders = [{ "id": "0",
            "name": "Item1",
            "price": 500,
            "quantity": 5,
        }]
