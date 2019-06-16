#Dropdown menu
from tkinter import *
start=Tk()
start.geometry("1050x600+200+100")#start.geometry("widthxheight+dist from x axis + dist from y axis")
def do():
    print("New file opened")
#creating main menu
main_menu=Menu(start)
start.config(menu=main_menu)
#creating file menu
file_menu=Menu(main_menu)
main_menu.add_cascade(label="File",menu=file_menu)
#creating edit menu
edit_menu=Menu(main_menu)
main_menu.add_cascade(label="Edit",menu=edit_menu)
#creating content in file menu
file_menu.add_command(label="New",command=do)
file_menu.add_command(label="Open",command=do)
file_menu.add_separator()
file_menu.add_command(label="Save",command=do)
file_menu.add_command(label="Close",command=do)
#creating menu inside menu
save_menu=Menu(file_menu)
file_menu.add_cascade(label='CTRL+S',menu=save_menu)
save_menu.add_command(label="NormalSave",command=do)
save_menu.add_command(label="SaveWithPassword",command=do)
start.mainloop()
