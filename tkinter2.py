#from tkinter import  *
start=Tk()
frame=Frame(start,width=300,height=500)#creating an invisible container
button1=Button(frame,text="button1")
button1.pack(side=LEFT)
button2=Button(frame,text="button2")
button2.pack(side=LEFT)
frame.pack()
bottomframe=Frame(start)
button3=Button(bottomframe,text="button3")
button3.pack()
bottomframe.pack(side=BOTTOM)

start.mainloop()Frames are invisible container in which we can group many components
