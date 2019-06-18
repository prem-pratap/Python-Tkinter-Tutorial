#Labelframe tutorial
from tkinter import *
start=Tk()
frame=LabelFrame(start,text="First LabelFrame",padx=5,pady=5)
entry=Entry(frame)
entry.pack()
frame.pack()
start.geometry("300x300+100+100")
start.mainloop()
