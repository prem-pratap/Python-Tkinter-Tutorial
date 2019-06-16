#there are three geometry managers in tkinter 1.grid 2.pack 3.place
from tkinter import *
start=Tk()
start.geometry("300x300+120+120")
label1=Label(start,text="hello")
label2=Label(start,text="world")
label1.place(x=10,y=10)#x is dist. from x axis and y is dists from y axis
label2.place(x=100,y=100)
start.mainloop()
