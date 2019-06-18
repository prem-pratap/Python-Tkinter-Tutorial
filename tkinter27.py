#scroll bar e.g2
from tkinter import *
start=Tk()
frame=Frame(start)
scroll=Scrollbar(frame)
scroll.pack(side=RIGHT,fill=Y)
l=Listbox(frame,yscrollcommand=scroll.set)
for i in range(1,100):
    l.insert(END,"List"+str(i))
l.pack(side=LEFT)
scroll.config(command=l.yview)
start.geometry("300x300+100+100")
frame.pack()
start.mainloop()
