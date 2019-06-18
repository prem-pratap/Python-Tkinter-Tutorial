#Input through pop window
from tkinter import *
from tkinter import simpledialog
start=Tk()
def getme():
    s=simpledialog.askstring("Input String","Enter Your Name")
    print(s)
butt=Button(start,text="popup",command=getme)
butt.pack()
start.geometry("300x300+100+100")
start.mainloop()
