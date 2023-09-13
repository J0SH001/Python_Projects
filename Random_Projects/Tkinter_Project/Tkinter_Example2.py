from tkinter import *

win = Tk()
v = StringVar()
v.set("this is set by the program")
e = Entry(win, textvariable = v)
e.pack()
