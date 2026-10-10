import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rajsingh9142@",
    database = "library_db"
)

cursor = conn.cursor()

title = input("enter book tilte:")

query = "select * from books where title = %s"

cursor.execute (query,(title,))

book = cursor.fetchone()

if book:
    print("\nbook foound!")
    print("book id :",book[0])
    print("title :",book[1])
    print("author:",book[2])
    print("quantity:",book[3])

else:
    print("book not found!")

cursor.close()
conn.close()        