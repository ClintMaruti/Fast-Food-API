import os
import psycopg2
from config import Config
from flask import current_app, jsonify

from tables import queries

def connect():
    conn = None
    try:

        print("Connecting to the PostgreSQL database...")
        DATABASE = os.getenv('DATABASE_URL')
        conn = psycopg2.connect(DATABASE)

        #create cursor
        cur = conn.cursor()

        # cur.execute('DROP TABLE users')
        # create tables 
        for query in queries:
            cur.execute(query)
       
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)
        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        response = jsonify({"Database Error":error})
    finally:
        if conn is not None:
            print('Database connected Successfully.')
            print('Tables Created Successfuly.')
    return conn

if __name__ == '__main__':
    connect()
