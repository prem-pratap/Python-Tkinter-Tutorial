#Checkbox eg 2
from tkinter import *
def clickme():
    print(i.get())
start=Tk()
start.geometry("300x300+100+100")
i=StringVar()
c=Checkbutton(start,text="First Option",variable=i,offvalue="unchecked",onvalue="checked")
c.pack()
butt=Button(start,text="click",command=clickme)
butt.pack()
start.mainloop()
