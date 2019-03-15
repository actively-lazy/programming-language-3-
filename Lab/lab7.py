import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mBox


def cmdExit():
    exit()


def cmdClear():
    svName.set("")
    svContact.set("")
    txtName.focus()


def cmdAdd():
    name = "Login User: " + str(svName.get())
    mBox.showinfo("Login User: ", name)


def cmdShowDetails():
    pass


# Tkinter Initialised
root = Tk()
root.geometry("480x360")
root.title("Contact Details")
# Initialising Tabpane(Notebook)
tabControl = ttk.Notebook(root)
tabAdd = ttk.Frame(tabControl)
tabControl.add(tabAdd, text="Insert Details")
tabControl.pack(expand=1, fill="both")
tabSearch = ttk.Frame(tabControl)
tabControl.add(tabSearch, text="Search")
tabUpdate = ttk.Frame(tabControl)
tabControl.add(tabUpdate, text="Update")
tabDelete = ttk.Frame(tabControl)
tabControl.add(tabDelete, text="Delete")

svName = StringVar()
svContact = StringVar()
svCity = StringVar()
svSearch = StringVar()
lblName = Label(tabAdd, text="Name: ", padx=3, pady=2)
lblName.grid(row=0, column=0)
txtName = ttk.Entry(tabAdd, textvariable=svName)
txtName.grid(row=0, column=1)
lblContact = Label(tabAdd, text="Contact: ", padx=3, pady=2)
lblContact.grid(row=2, column=0)
txtContact = ttk.Entry(tabAdd, textvariable=svContact)
txtContact.grid(row=2, column=1)
lblCity = Label(tabAdd, text="City: ", padx=3, pady=2)
lblCity.grid(row=3, column=0)
txtCity = ttk.Entry(tabAdd, textvariable=svCity)
txtCity.grid(row=3, column=1)
btnAdd = Button(tabAdd, text="Add", command=cmdAdd)
btnAdd.grid(row=4, column=0)
btnClear = Button(tabAdd, text="Clear", command=cmdClear, padx=3, pady=2)
btnClear.grid(row=4, column=1)
btnExit = Button(tabAdd, text="Exit", command=cmdExit, padx=3, pady=2)
btnExit.grid(row=4, column=2)
txtName.focus()
# Button Tab
lblSearch = Label(tabSearch, text="Search: ", padx=3, pady=2)
lblSearch.grid(row=0, column=0)
lblSearch = ttk.Entry(tabSearch, textvariable=svSearch)
lblSearch.grid(row=0, column=1)
btnSearch = Button(tabSearch, text="Search", padx=3, pady=2)
btnSearch.grid(row=1, column=1)

root.mainloop()
