import datetime
from flask import jsonify, sessions, request
import psycopg2

from db import connect

class Order(object):
    """This class defines the Order Models"""
    def __init__(self, name=None, price=None, quantity=None):
        """ A method constructor to define Order"""
    
        self.name = name
        self.price = price
        self.quantity = quantity

    def all_order(self):

        try:
                connection = connect()
                cur = connection.cursor()

                cur.execute("SELECT * from orders")
                orders = cur.fetchall()

                return {"Orders": orders}
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_order(self, order_id, name, price, quantity):
        """ Model function to Insert a new Order into list """
        sql = ("""INSERT INTO orders (order_id, name, price, quantity)
                    VALUES (%s, %s, %s, %s); """,
                    (self.order_id,self.name,self.price,self.quantity))

        try:
                connection = connect()
                cur = connection.cursor()
                
                cur.execute("SELECT * FROM orders WHERE (order_id)")

                orderID = cur.fetchone()

                if not orderID:
                    cur.execute(sql)
                else:
                    return {"Message": "Order already Exists! "}

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def order_id(self, order_id):
        """ Model function to GET a specific order list """

        try:

            connection = connect()
            cur = connection.cursor()
                
            cur.execute("SELECT * FROM orders WHERE (order_id)")

            orderID = cur.fetchone()
            return orderID
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def order_update(self, order_id, name, price, quantity):
        """ Model function to Update a specific order list """
        sql = ("""UPDATE orders
                SET name = %s, price = %s, quantity = %s
                WHERE order_id = %s""",
                (self.order_id,self.name,self.price,self.quantity))
        try:
            connection = connect()
            cur = connection.cursor()

            cur.execute(sql)
            orderUpdate = cur.fetchone
            return orderUpdate
    
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
