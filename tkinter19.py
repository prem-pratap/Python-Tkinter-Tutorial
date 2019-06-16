#Checkbox
from tkinter import *
def clickme():
    print(i.get())
start=Tk()
start.geometry("300x300+100+100")
i=IntVar()
c=Checkbutton(start,text="First Option",variable=i)
c.pack()
butt=Button(start,text="click",command=clickme)
butt.pack()
start.mainloop()
