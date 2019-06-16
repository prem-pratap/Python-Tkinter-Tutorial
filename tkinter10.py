#Working with messagebox
from tkinter import *
from tkinter import messagebox
def success():
    messagebox.showinfo("Success","Installation Complete")#arguements are ("Title","Message")
def error():
    messagebox.showerror("Oops","Installation Failed")#arguements are ("Title","Message")
def warning():
    messagebox.showwarning("Waring","Installation Paused")#arguements are ("Title","Message")

start=Tk()
butt=Button(start,text="Ok",command=success)
butt.pack()
butt2=Button(start,text="Fault",command=error)
butt2.pack()
butt3=Button(start,text="Warning",command=warning)
butt3.pack()

start.geometry("200x200+200+200")
start.mainloop()
