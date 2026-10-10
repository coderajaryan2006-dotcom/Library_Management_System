from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()

root.title("View Books")
root.geometry("700x400")

tree = ttk.Treeview(root)

tree["columns"] = ("ID","Title","Author","Quantity")

tree.column("#0", width=0, stretch=NO)

tree.column("ID", width=80)
tree.column("Title", width=200)
tree.column("Author", width=200)
tree.column("Quantity", width=100)

tree.heading("ID", text="Book ID")
tree.heading("Title", text="Title")
tree.heading("Author", text="Author")
tree.heading("Quantity", text="Quantity")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rajsingh9142@",
    database="library_db"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM books")

rows = cursor.fetchall()

for row in rows:
    tree.insert("", END, values=row)

tree.pack(fill=BOTH, expand=True)

cursor.close()
conn.close()

root.mainloop()