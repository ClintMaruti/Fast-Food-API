from datetime import datetime, timedelta
from flask import Flask
from flask import jsonify, sessions, request
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from flask_jwt_extended import create_access_token
import psycopg2

from db import connect

class Order(object):
    """This class defines the Order Models"""
    def __init__(self, name=None, price=None, quantity=None,status = None,date=None):
        """ A method constructor to define Order"""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.status = status
        self.date = datetime.now().replace(second=0, microsecond=0)


    def place_order(self):
        """ Model function to place an order for food """
        try:

            connection = connect()
            cur = connection.cursor()
            #Execute query
            cur.execute('INSERT INTO orders (name,price,quantity,status,date) VALUES(%s,%s, %s, %s, %s)', (self.name, self.price, self.quantity, self.status, self.date))
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

                return jsonify({"Orders": orders})
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

            cur.execute(sql)

            cur.close()
            # commit the changes
            connection.commit()

            orderUpdate = cur.fetchone
            return orderUpdate
    
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
########### User Section ###########
class User(object):
    def __init__(self,password,name, email=None, admin=None, date=None):
        self.name = name
        self.email = email
        self.password = password
        self.admin = admin
        self.date = datetime.now().replace(second=0, microsecond=0)
        print(self.password)
  
    def hash_password(self, password):
        hashlized = self.password_hash = pwd_context.encrypt(password)
        return hashlized

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
    
    def getusername(self, username):
        """
            Fetchs userobject by name from the database
        """
        try:
            connection = connect()
            cur = connection.cursor()
            #Execute query
            cur.execute("SELECT user_name FROM users WHERE user_name='{}'".format(username))
            userobject = cur.fetchone()
            if not userobject:
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
            cur.execute("SELECT user_name, password FROM users WHERE user_name='{}'".format(self.name))
            userobject = cur.fetchone()
            # print("Message:", self.password, userobject)
            pass_verify = pwd_context.verify(self.password,userobject[1])
            # print(pass_verify)
            if userobject[0] == self.name and pass_verify == True:
                print("test")
                expires = timedelta(minutes=60)
                token = create_access_token(identity=self.name, expires_delta=expires )
                      
                return jsonify({"Message: ": "Login Succesful"})
            
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
    

    def generate_auth_token(self, expiration = 600):
        s = Serializer('secretkey', expires_in = expiration)
        return s.dumps({ 'id': self.name })

    @staticmethod
    def verify_auth_token(token):
        s = Serializer('secretkey')
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        
        return jsonify({"Message":"Invalid"})

########### Food Menu ###########
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
            