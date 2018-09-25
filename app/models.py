import datetime

now = datetime.datetime.now()

class Orders(object):
  def __init__(self):
    self.orders = [
      { "id": 0,
        "name": "Urban Burger",
        "price": 800,
        "status": "Delivered"
      }
    ]
    self.food_order_count = 1
  
  def all_order(self):
    return self.orders

  def insert_order(self, order_info):
    """ Model function to Insert a new Order int list """
    if isinstance(order_info, dict):
      order_info['date'] = now
      order_info['status'] = 'Delayed'
      self.orders = order_info
      self.food_order_count += 1

      return {'message': 'Thank You. Your Order has been placed successfuly! '}
    return {"message": 'Order Rejected!!!'}
  
  def order_id(self, order_id):
    if isinstance(order_id, int):
      if order_id in self.orders:
        return self.orders[order_id]
      else:
        return {'message': 'Order Not available'}
  
  def order_update(self, order_id, update_status):
    if isinstance(order_id, int):
      if order_id in self.orders:
        self.orders['status'] =  update_status
        return {"message: ": "Order Status Updates Successfully"}
      return {"message": "There has been an error in your update"}
