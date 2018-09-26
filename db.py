import os
import psycopg2
from config import Config
import sys

ft = Config()

def connect():
    conn = None
    try:
        #read connection parameters
        params = ft.config()

        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(host="localhost", database="alpha", user="machiatto", password="admin@234" )

        #create cursor
        cur = conn.cursor()

         # create table one by one
        cur.execute("""CREATE TABLE orders(
            order_id serial PRIMARY KEY,
            name VARCHAR NOT NULL,
            price VARCHAR NOT NULL,
            quantity VARCHAR NOT NULL);""")



        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print('Database connected Successfully.')
            print('Tables Created Successfuly.')



if __name__ == '__main__':
    connect()
