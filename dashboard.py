from tkinter import *
import os



def add_book():
    os.system("python Library_Management_System/add_book_gui.py")

def view_book():
    os.system("python Library_Management_System/view_books_gui.py")

def search_book():
    os.system("python Library_Management_System/search_book_gui.py")

def update_book():
    os.system("python Library_Management_System/update_book_gui.py")

def delete_book():
    os.system("python Library_Management_System/delete_book_gui.py")




root = Tk()

root.title("Library Management System")
root.geometry("500x500")
root.config(bg="lightblue")

Label(
    root,
    text="LIBRARY MANAGEMENT SYSTEM",
    font=("Arial",20,"bold"),
    bg="lightblue"
).pack(pady=20)

Button(root,text="Add Book",
       width=20,
       command=add_book).pack(pady=10)

Button(root,text="View Books",
       width=20,
       command=view_book).pack(pady=10)

Button(root,text="Search Book",
       width=20,
       command=search_book).pack(pady=10)

Button(root,text="Update Book",
       width=20,
       command=update_book).pack(pady=10)

Button(root,text="Delete Book",
       width=20,
       command=delete_book).pack(pady=10)

Button(root,
       text="Exit",
       width=20,
       command=root.destroy).pack(pady=20)

root.mainloop()