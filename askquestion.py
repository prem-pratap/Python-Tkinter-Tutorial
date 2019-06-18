#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
start=Tk()
def callme():
    get=messagebox.askquestion("Exit","Do you really want to exit?")
    if get=='yes':
        start.quit()

start.geometry('200x200+200+200')
butt=Button(start,text="Ok",command=callme)
butt.pack()
start.mainloop()
