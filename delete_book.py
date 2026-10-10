import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rajsingh9142@",   
    database="library_db"
)

cursor = conn.cursor()


book_id = int(input("Enter Book ID to Delete: "))


query = "DELETE FROM books WHERE book_id = %s"


cursor.execute(query, (book_id,))


conn.commit()


if cursor.rowcount > 0:
    print("Book Deleted Successfully!")
else:
    print("Book ID Not Found!")


cursor.close()
conn.close()