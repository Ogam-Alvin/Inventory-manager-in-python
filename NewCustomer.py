import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox


def cancel():
    root.destroy()
    import CustomerLogin


db = mysql.connector.connect(host="localhost", user="root", password="root", db="admin")


def create():
    mycursor = db.cursor()
    Name = e1.get()
    Password = e2.get()
    Email = e3.get()
    Contact = e4.get()
    if Name=='':
        messagebox.showinfo("Fill Missing Field(s)")
    if Password=='':
        messagebox.showinfo("Fill Missing Field(s)")
    if Email=='':
        messagebox.showinfo("Fill Missing Field(s)")
    if Contact=='':
        messagebox.showinfo("Fill Missing Field(s)")
        root.destroy()


    mycursor.execute("insert into customers(Name, Password, Email, Contact) values( '"+Name+"', '"+Password+"', '"+Email+"', '"+Contact+"')")
    db.commit()
    root.destroy()
    import UserLogInSystem


root=tk.Tk()
root.title(" Customer Registration")
root.geometry("300x200")

Label(root, text="Name").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)
Label(root, text="Email").place(x=10, y=70)
Label(root, text="Contact").place(x=10, y= 100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

Button(root, text="Create", command=create).place(x=10, y=160)
Button(root, text="Cancel", command=cancel).place(x=210, y=160)

root.mainloop()