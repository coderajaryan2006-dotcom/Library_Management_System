from tkinter import *


from tkinter import *

# ===========================
# Button Functions
# ===========================

def add_book():
    print("Add Book Clicked")

def view_books():
    print("View Books Clicked")

def search_book():
    print("Search Book Clicked")

def update_book():
    print("Update Book Clicked")

def delete_book():
    print("Delete Book Clicked")

# ===========================
# Main Window
# ===========================

root = Tk()
root.title("Library Management System")
root.geometry("700x500")
root.config(bg="lightblue")

# Heading
heading = Label(
    root,
    text="LIBRARY MANAGEMENT SYSTEM",
    font=("Arial", 22, "bold"),
    bg="lightblue",
    fg="darkblue"
)
heading.pack(pady=20)

# Buttons
Button(root, text="Add Book", width=20, command=add_book).pack(pady=10)

Button(root, text="View Books", width=20, command=view_books).pack(pady=10)

Button(root, text="Search Book", width=20, command=search_book).pack(pady=10)

Button(root, text="Update Book", width=20, command=update_book).pack(pady=10)

Button(root, text="Delete Book", width=20, command=delete_book).pack(pady=10)

Button(root, text="Exit", width=20, command=root.destroy).pack(pady=20)

root.mainloop()