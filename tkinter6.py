#Binding functions to button
from tkinter import *
start=Tk()
def callme():
    print("Hey Dude!!!!")
def second(event):
    print("Second Method")
button=Button(start,text="Click me",command=callme)
button2=Button(start,text="SecondMethod")
button2.bind("<Button-1>",second)#Function is called on left mouse click
button.pack()
button2.pack()
start.mainloop()

