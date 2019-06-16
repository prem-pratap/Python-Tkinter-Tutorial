#Canvas create line
from tkinter import *
start=Tk()
start.geometry('400x400+300+300')
canv=Canvas(start,width=300,height=400,bg="red")
line=canv.create_line(0,0,200,200)
canv.pack()
start.mainloop()
