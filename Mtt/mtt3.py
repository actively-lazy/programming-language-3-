# import time
# import Tkinter
#
# root = Tk()
# root.title("MTT3")
#
#
# listbox = Listbox(root)
#
#
# lbl.pack()
# listbox.pack()
#
# root.mainloop()
from Tkinter import *

top = Tk()
top.title("MTT3 Karunesh")

lbl = Label(top, text="Subjects in Semester 6")
lb2 = Label(top, text="Select the Subjects you want")
lb3 = Label(top, text="Selected: ")
listbox = Listbox(top, selectmode='multiple')

listbox.insert(1, "FWT")
listbox.insert(3, "IP")
listbox.insert(2, "OOSE")
listbox.insert(4, "SP")
listbox.insert(5, "PL3")
listbox.insert(6, "IEM")
listbox.insert(7, "BV")


def show_list(event=None):
    selected_text_list = [listbox.get(i) for i in listbox.curselection()]
    # print(selected_text_list)
    lb3.config(text="Selected: "+str(selected_text_list))

btn = Button(top, text="Select", fg="red",
             command=show_list)
lbl.pack()
lb2.pack()
listbox.pack()
lb3.pack()
btn.pack()
top.mainloop()
