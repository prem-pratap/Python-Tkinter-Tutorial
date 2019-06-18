#Working with multiple windows
from tkinter import *
start=Tk()
def openwindow():
    top=Toplevel()
    top.title('New Window')
    top.geometry("200x200+140+140")
    butt1=Button(top,text="Close",command=top.destroy)
    butt1.pack()
butt=Button(start,text="open window",command=openwindow)
butt.pack()
start.geometry("300x300+100+100")
start.mainloop()
