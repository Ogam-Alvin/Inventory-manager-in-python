import tkinter as tk
from tkinter import ttk
from tkinter import*
import mysql.connector

root = tk.Tk()
root.title("Products available")
root.geometry("810x300")


def show():
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="food")
    c = db.cursor()
    c.execute("select *from products")
    records=c.fetchall()
    print(records)
    db.commit()
    db.close()

style = ttk.Style()
style.theme_use("default")
tframe = Frame(root)
tframe.pack(pady=10)
tscroll = Scrollbar(tframe)
tree = ttk.Treeview(tframe, show= 'headings',columns = ('Product ID', 'Product Category', 'Product Name', 'Product Cost', 'Date of Manufacture', 'Products Available'),
 yscrollcommand=tscroll.set, selectmode="extended")

tree.pack()
tscroll.config(command=tree.yview)

tree.column("#0", width=0, stretch=NO)
tree.column("Product ID",anchor=W, width=140)
tree.column("Product Category",anchor=W, width=140)
tree.column("Product Name",anchor=W, width=140)
tree.column("Product Cost",anchor=W, width=140)
tree.column("Date of Manufacture",anchor=W, width=140)
tree.column("Products Available",anchor=W, width=140)

tree.heading("#0", text="", anchor=W)
tree.heading("Product ID", text="Product Id", anchor=W)
tree.heading("Product Category", text="Product Category", anchor=W)
tree.heading("Product Name", text="Product Name", anchor=W)
tree.heading("Product Cost", text="Product Cos", anchor=W)
tree.heading("Date of Manufacture", text="Date of Manufacture", anchor=W)
tree.heading("Products Available", text="Products Available", anchor=W)

def exit():
    root.destroy()
Button(root, text="Close", command=exit ).place(x=400, y=250)

show()
root.mainloop()