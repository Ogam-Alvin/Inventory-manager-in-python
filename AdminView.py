import tkinter as tk
from tkinter import ttk
import mysql.connector

def show():
    db=mysql.connector.connect(host="localhost", user="root", password="root", database="admin")
    mycursor=db.cursor()
    mycursor.execute("SELECT AdminId, Name FROM administartors")
    records=mycursor.fetchall()
    print(records)

    for i, (AdminID,Name) in enumerate(records, start=1):
        Listbox.insert("", "end", values=(AdminID, Name))
        db.close()


root = tk.Tk()
root.title("ADMIN RECORDS")
tk.Label(root, text="ADMIN RECORDS").grid(row=0, column=3)

cols=('AdminID', 'Name')
Listbox=ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    Listbox.heading(col, text=col)
    Listbox.grid(row=1, column=0, columnspan=2)
closebutton=tk.Button(root, text="Close", width=15, command=exit).grid(row=4, column=1)
show()
root.mainloop()



