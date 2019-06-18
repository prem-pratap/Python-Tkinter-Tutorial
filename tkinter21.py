#Radio button
from tkinter import *
def clickme():
    if i.get()==1:
        print("You have selected first option")
    else:
        print("You have selected second option")
start=Tk()
start.geometry("300x300+100+100")
i=IntVar()
r1=Radiobutton(start,text="First Option",value=1,variable=i)
r1.pack()
r2=Radiobutton(start,text="Second Option",value=2,variable=i)
r2.pack()

butt=Button(start,text="click",command=clickme)
butt.pack()
start.mainloop()
