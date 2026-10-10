from tkinter import *
from tkinter import messagebox
import mysql.connector


def save_book():

    title = title_entry.get()
    author = author_entry.get()
    quantity = quantity_entry.get()

    if title == "" or author == "" or quantity == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rajsingh9142@",
        database="library_db"
    )

    cursor = conn.cursor()

    query = """
    INSERT INTO books(title, author, quantity)
    VALUES(%s,%s,%s)
    """

    cursor.execute(query, (title, author, quantity))
    conn.commit()

    cursor.close()
    conn.close()

    messagebox.showinfo("Success", "Book Added Successfully")

    title_entry.delete(0, END)
    author_entry.delete(0, END)
    quantity_entry.delete(0, END)


root = Tk()

root.title("Add Book")
root.geometry("400x300")

Label(root, text="Book Title").pack(pady=5)
title_entry = Entry(root, width=30)
title_entry.pack()

Label(root, text="Author").pack(pady=5)
author_entry = Entry(root, width=30)
author_entry.pack()

Label(root, text="Quantity").pack(pady=5)
quantity_entry = Entry(root, width=30)
quantity_entry.pack()

Button(root,
       text="Save Book",
       command=save_book,
       width=20,
       bg="green",
       fg="white").pack(pady=20)

root.mainloop()