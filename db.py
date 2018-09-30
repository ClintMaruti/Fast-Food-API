import os
import psycopg2
from config import Config
import sys


from tables import queries


def connect():
    conn = None
    try:

        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(host="localhost", database="alpha", user="machiatto", password="admin@234" )

        #create cursor
        cur = conn.cursor()

        

        # create table one by one
        for query in queries:
            cur.execute(query)

        # #load sample data
        # name = 'Clint'
        # email = 'cmaruti93@gmail.com'
        # password = 'admin'
        # token = 'laksjdbfkjab'
        # role = 1

        # cur.execute('INSERT INTO users (user_name,email,password,role,token) VALUES(%s, %s, %s,%s,%s)', (name, email, password,role,token))

        # cur.execute('DROP TABLE users')
        
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
    return conn



if __name__ == '__main__':
    connect()
