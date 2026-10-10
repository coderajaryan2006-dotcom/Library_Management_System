from tkinter import *
from tkinter import messagebox
import mysql.connector

# Search Function
def search_book():

    title = title_entry.get()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rajsingh9142@",
        database="library_db"
    )

    cursor = conn.cursor()

    query = "SELECT * FROM books WHERE title=%s"

    cursor.execute(query, (title,))

    book = cursor.fetchone()

    if book:
        result.config(
            text=f"""
Book ID : {book[0]}

Title : {book[1]}

Author : {book[2]}

Quantity : {book[3]}
"""
        )

    else:
        messagebox.showerror("Error", "Book Not Found")

    cursor.close()
    conn.close()


# GUI
root = Tk()

root.title("Search Book")
root.geometry("400x350")

Label(root, text="Enter Book Title", font=("Arial", 12)).pack(pady=10)

title_entry = Entry(root, width=30)
title_entry.pack()

Button(
    root,
    text="Search",
    command=search_book,
    bg="blue",
    fg="white"
).pack(pady=15)

result = Label(root, text="", font=("Arial", 12))
result.pack()

root.mainloop()