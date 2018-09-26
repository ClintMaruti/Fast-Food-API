import datetime
from flask import jsonify, sessions


class Orders(object):
  """ Class that Holds methods for the endpoints """
  def __init__(self):
    """ We initialize an empty order list """
    self.order_list = []
    self.orernotfound = None
  
  def all_order(self):
    """ Model function that Fetchs all orders """
    if self.order_list == []:
      return ({"Message": "No Food Available.",
                "Bucket:": self.order_list})
    

  def insert_order(self, name, price, quantity):
    """ Model function to Insert a new Order int list """
    self.orders = {}

    self.orderId = len(self.order_list)
    self.orders['name'] = name
    self.orders['price'] = price
    self.orders['quantity'] = quantity
    self.orders['order_id'] = self.orderId + 1
    self.order_list.append(self.orders)
    return jsonify({"message": 'Your Order was placed successfully! ',
                    "Bucket: ":  self.order_list})
  
  def order_id(self, order_id):
    """ Model function to GET a specific order list """
    if isinstance(order_id, int):
      for order in self.order_list:
        if order['order_id'] == order_id:
          return jsonify({"message": "Success.", "Bucket": order})
        return {'message': 'Order Not available'}
  
  def order_update(self, order_id,name,price,quantity):
    """ Model function to Update a specific order list """
    if isinstance(order_id, int):
      for order in self.order_list:
        if order['order_id'] == order_id:
          order['name'] == name
          order['price'] == price
          order['quantity'] == quantity
          return jsonify({"message ": "Successful Update.",
          "Bucket: ": self.order_list}), 201
        return ({"Message": "Update not succesfull.", "Bucket, ": self.order_list})




