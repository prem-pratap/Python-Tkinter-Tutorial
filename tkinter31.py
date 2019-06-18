#Creating a spinbox
from tkinter import *
start=Tk()
def fetch():
    print(s.get())
s=Spinbox(start,from_=10,to=100)
s.pack()
butt=Button(start,text='Fetch',command=fetch)
butt.pack()
start.geometry("300x300+100+100")
start.mainloop()
