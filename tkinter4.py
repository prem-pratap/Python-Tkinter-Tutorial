#creating colored labels along with there size along x and y axis
from tkinter import *
start=Tk()
one= Label(start,text="one",bg="red")
two= Label(start,text="two",bg="blue")
three= Label(start,text="three",bg="green")
one.pack()
two.pack(fill=X)
three.pack(side=LEFT,fill=Y)
start.mainloop()
