#Color dialogbox
from tkinter import *
from tkinter import colorchooser
start=Tk()
def colorbox():
    clr=colorchooser.askcolor(title="Select Color")
    #print(clr)
    start.configure(background=clr[1])
butt=Button(start,text="Color Choose",command=colorbox)
butt.pack()
start.geometry("300x300+100+100")
start.mainloop()
