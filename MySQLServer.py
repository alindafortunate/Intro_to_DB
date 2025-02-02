from decouple import config
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host=config("host"),
        user=config("user"),
        password=config("password"),
        auth_plugin="mysql_native_password",
    )
    mycursor = mydb.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"
    mycursor.execute(sql)
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(e)
