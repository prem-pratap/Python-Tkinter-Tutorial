from tkinter import *
import wikipedia
start=Tk()
start.geometry("300x300+140+140")
def getme():
    entryvalue=entry.get()
    try:
        answer_value=wikipedia.summary(entryvalue)
        ans.delete(1.0,END)#this is done clear textbox on closing of 
        ans.insert(INSERT,answer_value)
    except:
        print("You Have Entered Wrong Input Or Check Your Internet Connection")
#creating a topframe
topframe=Frame(start)
topframe.pack(side=TOP)
entry=Entry(topframe)
entry.pack()
#creating a search
butt=Button(topframe,text="Search",command=getme)
butt.pack()
#creating scroll bar
bottomframe=Frame(start)
scroll=Scrollbar(bottomframe)
scroll.pack(side=RIGHT,fill=Y)
ans=Text(bottomframe,wrap=WORD,width=20,height=15,yscrollcommand=scroll.set)
scroll.config(command=ans.yview)
ans.pack()

bottomframe.pack(side=BOTTOM)

start.mainloop()
