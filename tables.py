
tb1 =  """ CREATE TABLE IF NOT EXISTS orders(
            order_id serial PRIMARY KEY,
            name VARCHAR NOT NULL,
            price REAL NOT NULL,
            quantity REAL NOT NULL);"""


tb2 = """ CREATE TABLE IF NOT EXISTS users(
            user_id SERIAL PRIMARY KEY NOT NULL,
            user_name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            admin BOOLEAN NOT NULL,
            token VARCHAR(255) NOT NULL

            );"""

tb3 = """ CREATE TABLE IF NOT EXISTS menu(
            menu_id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(255) NOT NULL,
            price REAL NOT NULL,
            description VARCHAR(255) NOT NULL,
            date TIMESTAMP

            );"""

queries = [tb1, tb2, tb3]
