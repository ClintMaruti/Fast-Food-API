import datetime
from flask import jsonify, sessions

orders = []

class Orders(object):
  """ Class that Holds methods for the endpoints """
  def __init__(self, name=None, price=None, quantity=None):
    """ We initialize an empty order list """
    self.id = len(orders) + 1
    self.name = name
    self.price = price
    self.quantity = quantity
  
  def all_order(self):
    """ Model function that Fetchs all orders """
    if orders == []:
      return ({"Message": "No Food Available.",
                "Bucket:": orders})
    

  def insert_order(self, name, price, quantity):
    """ Model function to Insert a new Order int list """
    self.bucketlist = {}

    self.bucketlist['name'] = name
    self.bucketlist['price'] = price
    self.bucketlist['quantity'] = quantity
    self.bucketlist['order_id'] = self.id
    orders.append(self.bucketlist)
    return jsonify({"message": 'Your Order was placed successfully! ',
                    "Bucket: ":  orders})
  
  def order_id(self, order_id):
    """ Model function to GET a specific order list """
    if isinstance(order_id, int):
      for order in orders:
        if order['order_id'] == id:
          return jsonify({"message": "Success.", "Bucket": order})
        return {'message': 'Order Not available'}
  
  def order_update(self, order_id,name,price,quantity):
    """ Model function to Update a specific order list """
    if isinstance(order_id, int):
      for order in orders:
        if order['order_id'] == id:
          order['name'] == name
          order['price'] == price
          order['quantity'] == quantity
          return jsonify({"message ": "Successful Update.",
          "Bucket: ": orders}), 201
        return ({"Message": "Update not succesfull.", "Bucket, ": orders})




