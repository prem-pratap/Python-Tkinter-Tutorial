#Storing entry values
#Method 1
from tkinter import *
start=Tk()
def clickme():
    print(entry.get())
start.geometry("300x300+100+100")
entry=Entry(start)
entry.pack()
butt=Button(start,text="Click Me",command=clickme)
butt.pack()
start.mainloop()

