import tkinter as tk
import mysql.connector
from tkinter import *
from subprocess import call
from tkinter import messagebox


def login():
    db = mysql.connector.connect(host="localhost", user="root", password="root",)
    import AdminLogInSystem
def ok():
    root.destroy()
    import MainPage

def register():
    root.destroy()
    import NewAdmin

root=tk.Tk()
root.title("Admin Login")
root.geometry("300x200")
Button(root, text="Login", command=login).place(x=10, y=10)
Button(root, text="Back", command=ok).place(x=210, y=160)
Button(root, text="Create Account",command=register).place(x=10, y=100)

root.mainloop()
