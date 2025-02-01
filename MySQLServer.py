# Write a simple python script that creates the database alx_book_store
# in your MySQL server.

# Name of python script should be MySQLServer.py
# If the database alx_book_store already exists, your script should not fail
# You are not allowed to use the SELECT or SHOW statements
# NOTE :

# Required to print message such as Database 'alx_book_store'
#  created successfully! when database is successfully created.

# Print error message to handle errors when failing to connect to the DB.

# handle open and close of the DB in your script.

# CREATE DATABASE IF NOT EXISTS alx_book_store
from decouple import config
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="alindafortunate",
        password=config("password"),
        database="alx_book_store",
    )
    mycursor = mydb.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"
    mycursor.execute(sql)

except mysql.connector.errors.NotSupportedError as e:
    print(e)
