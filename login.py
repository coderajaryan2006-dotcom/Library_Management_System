from tkinter import *
from tkinter import messagebox

# Login Function
def login():

    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful")
        root.destroy()

        # Open Dashboard
        import dashboard

    else:
        messagebox.showerror("Login", "Invalid Username or Password")


# Main Window
root = Tk()

root.title("Library Management System")
root.geometry("400x300")
root.config(bg="lightblue")

Label(
    root,
    text="LIBRARY LOGIN",
    font=("Arial",20,"bold"),
    bg="lightblue"
).pack(pady=20)

Label(root,text="Username",bg="lightblue").pack()

username_entry = Entry(root,width=30)
username_entry.pack()

Label(root,text="Password",bg="lightblue").pack()

password_entry = Entry(root,width=30,show="*")
password_entry.pack()

Button(
    root,
    text="Login",
    command=login,
    bg="green",
    fg="white",
    width=15
).pack(pady=20)

root.mainloop()