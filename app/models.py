import datetime

now = datetime.datetime.now()
ORDERS = []
ORDER_COUNT = 1

class Orders(object):
  """ Class that Holds methods for the endpoints """
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity
    self.food_order_count = 1
  
  def all_order(self):
    """ Model function that Fetchs all orders """
    if ORDERS == []:
      return {"Message": "No Food Available"}
    return ORDERS

  def insert_order(self, order_info):
    """ Model function to Insert a new Order int list """
    if isinstance(order_info, dict):
      order_info['date'] = now

      global ORDER_COUNT, ORDERS  
      ORDER_COUNT += 1
      ORDERS[ORDER_COUNT] = order_info 

      return {'message': 'Thank You. Your Order has been placed successfuly! '}
    return {"message": 'Order Rejected!!!'}
  
  def order_id(self, order_id):
    """ Model function to GET a specific order list """
    if isinstance(order_id, int):
      if order_id in ORDERS:
        return ORDERS[order_id]
      else:
        return {'message': 'Order Not available'}
  
  def order_update(self, order_id, update_status):
    """ Model function to Update a specific order list """
    if isinstance(order_id, int):
      if order_id in ORDERS:
        ORDERS['status'] =  update_status
        return {"message: ": "Order Status Updates Successfully"}
      return {"message": "There has been an error in your update"}
