import time
from tkinter import *


def create_rectangle(event=None):
    a = canvas.create_rectangle(50, 50, 400, 400, fill='red')


def create_circle(event=None):
    x, y, r, canvasName = 250, 600, 100, canvas
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill='green')


def quit_program(event=None):
    label.config(text="Thank You For Evaluating \n Quiting in 5 sec")
    root.update()
    time.sleep(5)
    root.quit()


root = Tk()
root.geometry("500x900")
root.title("MTT2")
label = Label(text="Aldridge Fonseca B222")
label.config(font=("Courier", 20))
label.pack()
canvas = Canvas(root, width=550, height=820, bg='black')
canvas.pack()

stateRectangle = False
stateCircle = False

c = root.bind('c', create_circle)
r = root.bind('r', create_rectangle)
q = root.bind('q', quit_program)
buttonRectangle = Button(root, text="Rectangle", fg="red", command=create_rectangle, underline=0)
buttonCircle = Button(root, text="Circle", fg="green", command=create_circle, underline=0)
buttonQuit = Button(root, text="Quit", fg="black", command=quit_program, underline=0)

buttonRectangle.pack(side=LEFT)
buttonCircle.pack(side=RIGHT)
buttonQuit.pack()

root.mainloop()
