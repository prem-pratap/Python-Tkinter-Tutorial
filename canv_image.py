#!/usr/bin/env python3
from tkinter import *
start=Tk()
canv=Canvas(start,width=700,height=500)
canv.pack()
photo=PhotoImage(file="/home/prem/Desktop/tkinter/take.png")
canv.create_image(0,0,image=photo,anchor=CENTER)#(dist.from x axis,dist. from y axis,image,anchor=position on canvas from where we want      #to start pic NW=NorthWest 
canv.pack()
start.mainloop()
