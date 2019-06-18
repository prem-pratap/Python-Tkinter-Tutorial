#Working with fonts
from tkinter import *
from tkinter.font import Font
start=Tk()
my_font=Font(family="Rekha",size=40,weight="bold",slant="italic",underline=0)#1 for underline
label=Label(start,text="Hello",font=my_font).pack()
start.geometry("300x300+120+120")
start.mainloop()
'''
to check complete font list
from tkinter import *
from tkinter.font import Font
start=Tk()
fonts=list(font.families())
for item in fonts:
    print(item)
'''
