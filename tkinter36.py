#How to bind shortcut keys with functions
from tkinter import *
from tkinter import messagebox
start=Tk()
#when we bind a function with start then we have to pass event as an arguement
#but if pass event like def callme(event) then error will occur when we clcik our button
#to resolve the method shown below is preferred
def callme(event=""):
    messagebox.showinfo("Trying","Wait this is important")
butt=Button(start,text="call Me",command=callme)
butt.pack()
start.bind('<Control-c>',callme)
start.geometry("300x300")
start.mainloop()
