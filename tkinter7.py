#Mouse click events
from tkinter import *
start=Tk()
def right_click(event):
    print("RightClick")
def left_click(event):
    print("leftClick")
def scroll(event):
    print("Scroll")
frame=Frame(start,width=300,height=300)
frame.bind("<Button-1>",left_click)
frame.bind("<Button-2>",scroll)
frame.bind("<Button-3>",right_click)
frame.pack()
start.mainloop()
