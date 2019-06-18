#Slider tutorial
from tkinter import *
start=Tk()
def fetch():
    print(s.get())
s=Scale(start,from_=0,to=100,length=200,width=25,sliderlength=20)#we can pass orient=HORIZONTAL for horizontal scale
#default length and width are 100 and 15 respectively
#default sliderlength is 30
butt=Button(start,text="Fetch",command=fetch)
butt.pack()
s.pack(side=RIGHT,fill=Y)
start.geometry("300x300+100+100")
start.mainloop()
