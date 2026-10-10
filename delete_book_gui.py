from tkinter import *
from tkinter import messagebox
import mysql.connector

def delete_book():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rajsingh9142@",
        database="library_db"
    )

    cursor = conn.cursor()

    book_id = id_entry.get()

    query = "DELETE FROM books WHERE book_id=%s"

    cursor.execute(query, (book_id,))

    conn.commit()

    if cursor.rowcount > 0:
        messagebox.showinfo("Success", "Book Deleted Successfully")
    else:
        messagebox.showerror("Error", "Book ID Not Found")

    cursor.close()
    conn.close()

    id_entry.delete(0, END)

root = Tk()

root.title("Delete Book")
root.geometry("350x220")

Label(root, text="Book ID", font=("Arial",12)).pack(pady=10)

id_entry = Entry(root, width=25)
id_entry.pack()

Button(
    root,
    text="Delete Book",
    command=delete_book,
    bg="red",
    fg="white",
    width=20
).pack(pady=20)

root.mainloop()