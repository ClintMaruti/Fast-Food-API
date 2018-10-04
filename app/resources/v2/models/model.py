from datetime import datetime, timedelta
from flask import Flask
from flask import jsonify, sessions, request
from passlib.apps import custom_app_context as pwd_context
                          
import psycopg2

from db import connect

class Order(object):
    """This class defines the Order Models"""
    def __init__(self,user_id=None, name=None, price=None, quantity=None,status = None,date=None):
        """ A method constructor to define Order"""
        self.user_id = user_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.status = status
        self.date = datetime.now().replace(second=0, microsecond=0)


    def place_order(self):
        """ Model function to place an order for food """
        sql = "INSERT INTO orders (name, price,quantity,status) VALUES(%s, %s, %s, %s, %s)", (self.name, self.price, self.quantity,self.date)

        try:

            connection = connect()
            cur = connection.cursor()
            #Execute query
            cur.execute('INSERT INTO orders (user_id,name,price,quantity,status,date) VALUES(%s,%s, %s, %s, %s,%s)', (self.user_id, self.name, self.price, self.quantity, self.status, self.date))
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            connection.commit()
            response = jsonify({"Message": "Order Updated Successfully"})
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    

    def all_order(self):
        """This function fetchs all orders"""
        try:
                connection = connect()
                cur = connection.cursor()

                cur.execute("SELECT * from orders")
                orders = cur.fetchall()

                return orders
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def order_id(self,id):
        """ Model function to GET a specific order list by Id"""

        try:
            connection = connect()
            cur = connection.cursor()                
            cur.execute("SELECT order_id, name, price, quantity, status date FROM orders WHERE order_id='{}'".format(id))
            order_by_ID = cur.fetchone()
            # print(order_by_ID)
            return order_by_ID       
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def order_update(self,order_id,status):
        """ Model function to Update a specific order list """
        sql = ("""UPDATE orders
                SET status = %s
                WHERE order_id = %s""",
                (status, order_id))
        try:
            connection = connect()
            cur = connection.cursor()

            cur.execute("UPDATE orders SET status='{}' WHERE order_id = '{}'".format(status,order_id))

            cur.close()
            # commit the changes
            connection.commit()

            orderUpdate = cur.fetchone
            return orderUpdate
    
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def order_history(self, user_id):
        """Model Function to get user order history"""
        try:
            connection = connect()
            cur = connection.cursor()

            cur.execute("SELECT order_id, name, price, quantity, status date FROM orders WHERE user_id='{}'".format(user_id))
            user_history = cur.fetchone()
            print(user_history)
            return user_history
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

########### User Section ###########
class User(object):

    def __init__(self,name,password,email=None,admin=None, date=None):
        self.name = name
        self.email = email
        self.password = password
        self.admin = admin
        self.date = datetime.now().replace(second=0, microsecond=0)
        print(self.password)
  
    def hash_password(self, password):
        hashlized = self.password_hash = pwd_context.encrypt(password)
        return hashlized

    def getusername(self, username):
        """
            Fetchs userobject by name from the database
        """
        try:
            connection = connect()
            cur = connection.cursor()
            #Execute query
            cur.execute("SELECT user_name FROM users WHERE user_name='{}'".format(username))
            userName= cur.fetchone()
            print (userName[0])
            print(username)
            if userName[0] == str(username):
                return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False

 
    def login(self):
        """
            This function verifies the user name and password for successful Login
        """
        try:
            connection = connect()
            cur = connection.cursor()
            #Exexcute Query
            cur.execute("SELECT user_name,email, password  FROM users WHERE user_name='{}'".format(self.name))
            userobject = cur.fetchone()
            if userobject[0] == self.name and userobject[1] == self.password:
                # print(self.password, userobject[1])          
                return True
            else:                
                return jsonify({"Message: ": "Invalid Login"}, 400)           
        except (Exception, psycopg2.DatabaseError) as error:
                       
            return jsonify({"Message: ": str(error)})

    def getallUser(self):
        """
            Fetchs and returns all users from the database
        """
        try:
            connection = connect()
            cur = connection.cursor()
            #Execute query
            cur.execute('SELECT * FROM users')
            all = cur.fetchall()
            return all
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    

    def addUser(self):
        """Adds a new user into the db"""    
        try:
            connection = connect()
            cur = connection.cursor()
            #Execute query
            cur.execute('INSERT INTO users (user_name,email,password,admin) VALUES(%s, %s, %s,%s)', (self.name, self.email, self.password,self.admin))

            cur.close()
            connection.commit()

            response = jsonify({"message": "User succeffuly added"})
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def delete(self,user_id):
        try:
            connection = connect()
            cur = connection.cursor()
            #Execute query
            cur.execute("DELETE FROM users WHERE user_id='{}'".format(user_id))

            cur.close()
            connection.commit()

            response = jsonify({"message": "User succeffuly Deleted"})
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

############# Food Menu ##########################
class FoodMenu(object):
    """model class For menu"""
    def __init__(self, name=None, price=None, description=None, date=None):
        """Contsructor Class"""
        self.name = name
        self.price = price
        self.description = description
        self.date = datetime.now().replace(second=0, microsecond=0)
    
    
    def insert_menu(self):
        """class method to insert new menu to the database"""
        try:
            connection = connect()
            cur = connection.cursor()
            #Execute query
            cur.execute('INSERT INTO menu (name,price,description,date) VALUES(%s,%s, %s, %s)', (self.name, self.price, self.description, self.date))
            cur.close()
            connection.commit()

            response = jsonify({"Message": "Menu Updated Successfully!"})
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_menu(self):
        """Method That fetches the menu from the database"""
        try:
            connectioin = connect()
            cur = connectioin.cursor()
            #Execute query
            cur.execute('SELECT * FROM menu')

            all = cur.fetchall()
            return all
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def delete(self,user_id):
        try:
            connection = connect()
            cur = connection.cursor()
            #Execute query
            cur.execute("DELETE FROM menu WHERE menu_id='{}'".format(user_id))

            cur.close()
            connection.commit()

            response = jsonify({"message": "Menu succeffuly Deleted"})
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            