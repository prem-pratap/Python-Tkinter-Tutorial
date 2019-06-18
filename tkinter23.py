#Creating a combobox
from tkinter import *
from tkinter.ttk import Combobox
start=Tk()
def selected():
    print(combo.get())
l=list(range(0,51))
combo=Combobox(start,values=l,height=20)#default width is 10
combo.set("Select")
combo.pack()
butt=Button(start,text="Selected",command=selected)
butt.pack()
start.geometry("300x300+120+120")
start.mainloop()
