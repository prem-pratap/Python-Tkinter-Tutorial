#Scrollbar
from tkinter import *
start=Tk()
scroll=Scrollbar(start)
scroll.pack(side=RIGHT,fill=Y)
l=Listbox(start,yscrollcommand=scroll.set)
for i in range(1,100):
    l.insert(END,"List"+str(i))
l.pack(side=LEFT)
scroll.config(command=l.yview)
start.geometry("300x300+100+100")
start.mainloop()
