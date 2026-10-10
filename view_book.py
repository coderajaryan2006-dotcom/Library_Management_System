import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rajsingh9142@",
    database = "library_db"
)

cursor = conn.cursor()

query = "select *from books"

cursor.execute(query)

books = cursor.fetchall()

print("\n------BOOS LIST-----")

for book in books:
    print(book)

cursor.close()
conn.close()    