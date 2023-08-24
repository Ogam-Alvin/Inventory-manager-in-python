#This page is used to choose who is login in to the system

import tkinter as tk
from tkinter import *

def admin():
    top.destroy()
    import AdminLogInSystem


def customer():
    top.destroy()
    import CustomerLogInSystem


def exit():
    top.destroy()



top=tk.Tk()
top.title("Home Page")
top.geometry("300x200")

Label(top, text="Welcome. Choose your Destination:").place(x=3, y=12)
Button(top, text="Admin", command=admin).place(x=10, y=70)
Button(top, text="Customer", command=customer).place(x=10, y=110)
Button(top, text="Exit", command=exit).place(x=260, y=160)

top.mainloop()