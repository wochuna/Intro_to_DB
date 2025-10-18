import mysql.connector
from mysql.connector import Error

try:
    # Establish a connection to the MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ChuiCube42KGBlue@"
    )

    mycursor = mydb.cursor()

    # Create the database
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close connections
    if mycursor:
        mycursor.close()
    if mydb.is_connected():
        mydb.close()
        print("Database connection closed.")