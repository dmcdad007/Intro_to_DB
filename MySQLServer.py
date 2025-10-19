# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server (adjust user and password as needed)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )
        cursor = conn.cursor()

        # Attempt to create the database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")

        # Close cursor and connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")

if __name__ == "__main__":
    create_database()
