import tkinter as tk
from tkinter import *
from tkinter import messagebox

import mysql.connector


def cancel():
    root.destroy()



db = mysql.connector.connect(host="localhost", user="root", password="root", db="admin")


def create():
    mycursor = db.cursor()
    Name = e1.get()
    Password = e2.get()
    ConfirmPassword = e3.get()
    if Name == '':
        messagebox.showinfo("Username Empty")

    if Password== '':
        messagebox.showinfo("Password Empty")

    if ConfirmPassword == '':
        messagebox.showinfo("Confirm Password")



    else:
        if Password==ConfirmPassword:
            mycursor.execute("insert into administartors(Name, Password, ConfirmPassword) values( '"+Name+"', '"+Password+"', '"+ConfirmPassword+"')")
            db.commit()
            db.close()
            messagebox.showinfo("Registration Succesfull")
            root.destroy()
        else:
            messagebox.showinfo("Password mismatch. Enter Again")


root=tk.Tk()
root.title(" Admin Registration")
root.geometry("300x200")

Label(root, text="Username").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)
Label(root, text=" Confirm Password").place(x=10, y=70)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

Button(root, text="Create", command=create).place(x=10, y=160)
Button(root, text="Cancel", command=cancel).place(x=210, y=160)

root.mainloop()