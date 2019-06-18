#File dialogbox tutorial
from tkinter import *
from tkinter import filedialog
start=Tk()
def file():
    result=filedialog.askopenfile(initialdir="/home/prem/Desktop/summer",title="Select file",filetypes=(("text files",".txt"),("All files","*")))
    for c in result:
        print(c)
start.geometry("300x300+100+100")
butt=Button(start,text="Open File",command=file)
butt.pack()
start.mainloop()
