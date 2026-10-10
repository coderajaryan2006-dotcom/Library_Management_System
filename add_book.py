import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "rajsingh9142@",
    database = "library_db"
)

cursor = conn.cursor()

title = input("enter book tilte:")
author = input("enter author name:")
quantity = int(input("enter quantity:"))

query = "INSERT INTO books(title,author,quantity) VALUES (%s,%s,%s)"

cursor.execute(query,(title,author,quantity))

conn.commit()

print("Book added successfully!")

cursor.close()
conn.close()