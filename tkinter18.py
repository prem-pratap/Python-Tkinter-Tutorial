#Storing entry values
#Method2
from tkinter import *
def clickme():
    s1=s.get()
    print(s1)
start=Tk()
start.geometry("300x300+100+100")
s=StringVar()
entry=Entry(start,textvariable=s)
s.set("welcome")
entry.pack()
butt=Button(start,text="Click Me",command=clickme)
butt.pack()
start.mainloop()

