#Save file dialogbox tutorial
from tkinter import *
from tkinter import filedialog
start=Tk()
def save_file():
    f=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if f is None:
        return
    else:
        f.write("Hello")
                                
start.geometry("300x300+100+100")
butt=Button(start,text="Save File",command=save_file)
butt.pack()
start.mainloop()
