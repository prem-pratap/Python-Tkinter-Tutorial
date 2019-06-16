#Message box more options
from tkinter import *
from tkinter import messagebox
start=Tk()
def callme():
    get=messagebox.askyesnocancel("Exit","Do you really want to exit?")
    print(get)
    if get:
        start.quit()
    

start.geometry('200x200+200+200')
butt=Button(start,text="Ok",command=callme)
butt.pack()
start.mainloop()
