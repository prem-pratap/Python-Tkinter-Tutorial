#Loading image through canvas.Image should be of the form png or gif
from tkinter import *
start=Tk()
canv=Canvas(start,width=700,height=500)
canv.pack()
photo=PhotoImage(file="/home/prem/Desktop/tkinter/take.png")
canv.create_image(0,0,image=photo,anchor=NW)
#(dist.from x axis,dist. from y axis,image,
#anchor=position on canvas from where we want to start our pic NW=NorthWest 
start.mainloop()
