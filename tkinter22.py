#Creating a listbox
from tkinter import *
def printitem():
    clickeditems=l.curselection()
    print(clickeditems)
    for item in clickeditems:
        print(l.get(item))
def delete():
    clickeditems=l.curselection()
    for item in clickeditems:
        print(l.delete(item))

start=Tk()
l=Listbox(start,width=30,height=20,selectmode=MULTIPLE)#default selectmode is BROWSE other are SINGLE EXTENDED
l.insert("1","C")
l.insert("2","C++")
l.insert("3","Python")
l.insert("4","Java")
l.insert("5","JS")
l.pack()
butt=Button(start,text="Print",command=printitem)
butt.pack()
butt_delete=Button(start,text="Delete",command=delete)
butt_delete.pack()
start.geometry("400x400+150+150")
start.mainloop()
