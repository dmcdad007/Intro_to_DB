import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the alx_book_store database if it does not already exist."""
    try:
        # Connect to MySQL Server (adjust user, password, and host as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         # 🔸 Replace with your MySQL username
            password="yourpassword"  # 🔸 Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure cursor and connection are closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
