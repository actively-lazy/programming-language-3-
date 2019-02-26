import time
from tkinter import *


def greaterthan():
    try:
        e2 = int(entry.get())
        e = int(entry2.get())
        if e > e2:
            label2.configure(text="{} is greater than {}".format(e, e2))
        else:
            label2.configure(text="{} is not greater than {}".format(e, e2))
    except:
        str = "invalid input"
        label2.configure(text=str)


def lessthan():
    try:
        e2 = int(entry.get())
        e = int(entry2.get())
        if e < e2:
            label2.configure(text="{} is less than {}".format(e, e2))
        else:
            label2.configure(text="{} is not less than {}".format(e, e2))
    except:
        str = "invalid input"
        label2.configure(text=str)


def equalthan():
    try:
        e2 = int(entry.get())
        e = int(entry2.get())
        if e == e2:
            label2.configure(text="{} is equal to {}".format(e, e2))
        else:
            label2.configure(text="{} is not equal to {}".format(e, e2))
    except:
        str = "invalid input"
        label2.configure(text=str)


def quit_program(event=None):
    label.config(text="Thank You For Evaluating \n Quiting in 5 sec")
    root.update()
    time.sleep(5)
    root.quit()


root = Tk()
root.title("MTT2")
label = Label(text="Aldridge Fonseca B222")
label.config(font=("Courier", 15))
label.grid(row=0, column=0)


label11 = Label(text="Inputs ------>")
label11.config(font=("Courier", 15))
label11.grid(row=1, column=0)
entry = Entry(root, bd=6)
entry.grid(row=1, column=1)


entry2 = Entry(root, bd=6)
entry2.grid(row=1, column=2)

label2 = Label(text="")
label2.config(font=("Courier", 15))
label2.grid(row=3, column=1)

buttonGreater = Button(root, text="Greater Than", fg="black",
                       command=greaterthan)
buttonLess = Button(root, text="Less Than", fg="black",
                    command=lessthan)
buttonEqual = Button(root, text="Equal to", fg="black",
                     command=equalthan)

buttonGreater.grid(row=2, column=0)
buttonLess.grid(row=2, column=1)
buttonEqual.grid(row=2, column=2)

# buttonQuit = Button(root, text="Quit", fg="black",
#                     command=quit_program, underline=0)
# buttonQuit.grid(row=,column=)
root.mainloop()
