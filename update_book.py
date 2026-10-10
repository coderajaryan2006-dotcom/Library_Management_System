import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rajsingh9142@",
    database = "library_db"
)

cursor = conn.cursor()

book_id = int(input("enter the book id to update:"))
new_title = input("enter the new book tilte:")
new_author = input("enter the new author name:")
new_quantity = int(input("enter new quantity"))


query = """
UPDATE books
SET title = %s,
    author = %s,
    quantity = %s
WHERE book_id = %s
"""

cursor.execute(query,(new_title,new_author,new_quantity,book_id))

conn.commit()
if cursor.rowcount >0:
    print("book update successfully!")
else:
    print("book id not found!")


cursor.close()
conn.close()        