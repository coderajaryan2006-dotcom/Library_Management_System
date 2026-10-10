import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rajsingh9142@",
    database="library_db"
)

print("Database Connected Successfully!")