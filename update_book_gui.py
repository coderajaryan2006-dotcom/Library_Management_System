from tkinter import *
from tkinter import messagebox
import mysql.connector


def update_book():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rajsingh9142@",
        database="library_db"
    )

    cursor = conn.cursor()

    query = """
    UPDATE books
    SET title=%s,
        author=%s,
        quantity=%s
    WHERE book_id=%s
    """

    values = (
        title_entry.get(),
        author_entry.get(),
        quantity_entry.get(),
        id_entry.get()
    )

    cursor.execute(query, values)
    conn.commit()

    if cursor.rowcount > 0:
        messagebox.showinfo("Success", "Book Updated Successfully")
    else:
        messagebox.showerror("Error", "Book ID Not Found")

    cursor.close()
    conn.close()


root = Tk()

root.title("Update Book")
root.geometry("400x350")

Label(root, text="Book ID").pack(pady=5)
id_entry = Entry(root, width=30)
id_entry.pack()

Label(root, text="New Title").pack(pady=5)
title_entry = Entry(root, width=30)
title_entry.pack()

Label(root, text="New Author").pack(pady=5)
author_entry = Entry(root, width=30)
author_entry.pack()

Label(root, text="New Quantity").pack(pady=5)
quantity_entry = Entry(root, width=30)
quantity_entry.pack()

Button(
    root,
    text="Update Book",
    command=update_book,
    bg="orange",
    fg="white"
).pack(pady=20)

root.mainloop()