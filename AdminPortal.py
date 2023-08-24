import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import*
import mysql
import mysql.connector

root = tk.Tk()
root.title("Products available")
root.geometry("810x510")


def mydb():
    db=mysql.connector.connect(host="localhost", user="root", password="root", database="food")
    c = db.cursor()

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
tree.heading("Product Cost", text="Product Cost", anchor=W)
tree.heading("Date of Manufacture", text="Date of Manufacture", anchor=W)
tree.heading("Products Available", text="Products Available", anchor=W)

dframe = LabelFrame(root, text="Records")
dframe.pack(fill="x", expand="yes", padx=20)


pidlabel = Label(dframe,text="Product ID")
pidlabel.grid(row=0, column=0, padx=10, pady=10)
pidentery= Entry(dframe)
pidentery.grid(row=0, column=1, padx=10, pady=10)

pclabel = Label(dframe,text="Product Category")
pclabel.grid(row=0, column=2, padx=10, pady=10)
pcentery= Entry(dframe)
pcentery.grid(row=0, column=3, padx=10, pady=10)

pnlabel = Label(dframe,text="Product Name")
pnlabel.grid(row=0, column=4, padx=10, pady=10)
pndentery= Entry(dframe)
pndentery.grid(row=0, column=5, padx=10, pady=10)

pcdlabel = Label(dframe,text="Product Cost")
pcdlabel.grid(row=1, column=0, padx=10, pady=10)
pcdentery= Entry(dframe)
pcdentery.grid(row=1, column=1, padx=10, pady=10)

domlabel = Label(dframe,text="Date of Manufacture")
domlabel.grid(row=1, column=2, padx=10, pady=10)
domentery= Entry(dframe)
domentery.grid(row=1, column=3, padx=10, pady=10)

palabel = Label(dframe,text="Products Available")
palabel.grid(row=1, column=4, padx=10, pady=10)
paentery = Entry(dframe)
paentery.grid(row=1, column=5, padx=10, pady=10)


def select(e):
    pidentery.delete(0, END)
    pcentery.delete(0, END)
    pndentery.delete(0, END)
    pcdentery.delete(0, END)
    domentery.delete(0, END)
    paentery.delete(0, END)

    selected = tree.focus()
    values = tree.item(selected, 'values')

    pidentery.insert(0, values[0])
    pcentery.insert(0, values[1])
    pndentery.insert(0, values[2])
    pcdentery.insert(0, values[3])
    domentery.insert(0, values[4])
    paentery.insert(0, values[5])


def update():
    selcted = tree.focus()
    tree.item(selcted, text="", values=(pidentery.get(), pcentery.get(), pndentery.get(), pcdentery.get(),domentery.get(), paentery.get()) )

    db = mysql.connector.connect(host="localhost", user="root", password="root", database="food")
    c = db.cursor()
    c.execute("""UPDATE products SET
    ProductCategory = :pca,
    ProductName = :pn,
    ProductCost = :pco,
    DateOfManufacture = :dom,
    ProductsAvailable = :pad
    
    WHERE oid = :oid""",{
        'pca': pcentery.get(),
        'pn': pndentery.get(),
        'pco': pcdentery.get(),
        'dom': domentery.get(),
        'pad': paentery.get(),
        'oid': pidentery.get(),
        }
              )
    c.commit()
    c.close()

    pidentery.delete(0, END)
    pcentery.delete(0, END)
    pndentery.delete(0, END)
    pcdentery.delete(0, END)
    domentery.delete(0, END)
    paentery.delete(0, END)

def show():
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="food")
    c = db.cursor()
    c.execute("select * from products")
    records=c.fetchall()
    global count
    count = 0
    for record in records:
        tree.insert(parent='', index='end', iid=count, values=(record[0], record[1], record[2], record[3], record[4], record[5]))
        count += 1


    db.commit()
    db.close()


def rem1():
    x = tree.selection()
    tree.delete(x)
    db=mysql.connector.connect(host="localhost", user="root", password="root", database="food")
    c = db.cursor()
    c.execute("DELETE from products WHERE ProductId=" + pidentery.get())
    db.commit()
    db.close()
    pidentery.delete(0, END)
    pcentery.delete(0, END)
    pndentery.delete(0, END)
    pcdentery.delete(0, END)
    domentery.delete(0, END)
    paentery.delete(0, END)

def remm():
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="food")
    c = db.cursor()

    db.commit()
    db.close()

def save():
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="food")
    c = db.cursor()

    pid=pidentery.get()
    proca =pcentery.get()
    prona=pndentery.get()
    proco=pcdentery.get()
    dom=domentery.get()
    prav =paentery.get()

    tree.insert(parent="", index="end", values=(pid, proca, prona, proco, dom, prav))

    db.commit()
    db.close()

def clear():
        pidentery.delete(0, END)
        pcentery.delete(0, END)
        pndentery.delete(0, END)
        pcdentery.delete(0, END)
        domentery.delete(0, END)
        paentery.delete(0, END)


def add():
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="food")
    c = db.cursor()
    c.execute("INSERT INTO 'products' ('ProductId', 'ProductCategory', 'ProductName', 'ProductCost', 'DateOfManufacture', 'ProductsAvailable') VALUES ('pid', 'proca', 'prona', 'proco', 'dom', 'prav');")
    db.commit()
    db.close()

bframe = LabelFrame(root, text="Command")
bframe.pack(fill="x", expand="yes", padx=30)

addbutton = Button(bframe, text="Add", command=save)
addbutton.grid(row=0, column=0, padx=10, pady=10)
r1button = Button(bframe, text="Remove", command=rem1)
r1button.grid(row=0, column=3, padx=10, pady=10)
updatebutton = Button(bframe, text="Update", command=update)
updatebutton.grid(row=0, column=7, padx=10, pady=10)
clearbutton = Button(bframe, text="Clear", command=clear)
clearbutton.grid(row=0, column=19, padx=10, pady=10)

def exit():
    root.destroy()
    import AdminLogin


Button(bframe, text="Close", command=exit ).grid(row=0, column=20, padx=10, pady=10)

tree.bind("<ButtonRelease-1>", select)

show()

root.mainloop()