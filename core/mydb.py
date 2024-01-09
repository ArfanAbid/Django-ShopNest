import mysql.connector

database=mysql.connector.connect(host='localhost',user='root',password='arfan123')
cursorObject=database.cursor()
# creating a database

cursorObject.execute("CREATE DATABASE mysql_database")

print("All SQL statements executed")
