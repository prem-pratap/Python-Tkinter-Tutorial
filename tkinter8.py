#Working with classes
from tkinter import *
class mybuttons():
    def __init__(self,master):
        self.printButton=Button(master,text="Print",command=self.printMessage)
        self.printButton.pack(side=LEFT)
        self.quitbutton=Button(master,text="Quit",command=master.quit)
        self.quitbutton.pack(side=LEFT)
    def printMessage(self):
        print("Heyy whatsupp")
start=Tk()
b=mybuttons(start)
start.mainloop()
