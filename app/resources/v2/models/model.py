from datetime import datetime
from flask import jsonify, sessions, request
from passlib.apps import custom_app_context as pwd_context

import psycopg2

from db import connect

class Order(object):
    """This class defines the Order Models"""
    def __init__(self, name=None, price=None, quantity=None, date=None):
        """ A method constructor to define Order"""

        self.name = name
        self.price = price
        self.quantity = quantity
        self.date = datetime.now().replace(second=0, microsecond=0)

    def insert_order(self):
        """ Model function to Insert a new Order int list """
        sql = "INSERT INTO orders (name, price, quantity, date) VALUES(%s, %s, %s, %s)", (self.name, self.price, self.quantity, self.date)

        try:

            connection = connect()
            cur = connection.cursor()
            #Execute query
            cur.execute(sql)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            cur.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def all_order(self):

        try:
                connection = connect()
                cur = connection.cursor()

                cur.execute("SELECT * from orders")
                orders = cur.fetchall()

                return jsonify({"Orders": orders})
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def order_id(self, order_id):
        """ Model function to GET a specific order list """

        try:

            connection = connect()
            cur = connection.cursor()
                
            cur.execute("SELECT * FROM orders WHERE WHERE id=%s", (order_id))

            orderID = cur.fetchall()
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
    
    def order_payload(self):    

        return dict(
            name =  self.name,
            price =  self.price,
            quantity =  self.quantity,
        )
    

class User(object):
    def __init__(self, name=None, email=None, password=None, admin=None, token=None, date=None):
        self.name = name
        self.email = email
        self.password = password
        self.admin = admin
        self.token = token
        self.date = datetime.now().replace(second=0, microsecond=0)
    
    def user_jsonloads(self):
        return dict(
            username= self.name,
            email=self.email,
            password=self.password,
            admin = self.admin,
            token = self.token,
            date = self.date,
        )

    def hash_password(self, password):
        hashlized = self.password_hash = pwd_context.encrypt(password)
        return hashlized

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
    
    def getusername(self, name):
        """
            Fetchs username
        """
        try:
            connection = connect()
            cur = connection.cursor()
            #Execute query
            cur.execute('SELECT * FROM users WHERE user_name=%s',(name))
            name = cur.fetchone()
            if name:
                return name
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def getpasword(self, password):
        """
            Fetchs passwords for verication during login
        """
        try:
            connection = connect()
            cur = connection.cursor()
            #Esxecute Query
            cur.execute('SELECT * FROM users WHERE password=%s', (password))
            password = cur.fetchone()
            if password:
                return password

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


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
            cur.execute('INSERT INTO users (user_name,email,password,admin,token) VALUES(%s, %s, %s,%s,%s)', (self.name, self.email, self.password,self.admin,self.token))

            cur.close()
            connection.commit()

            response = jsonify({"message": "User succeffuly added"})
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
