#Creating a text editor with tkinter
from tkinter import *
from tkinter import filedialog
start=Tk()

class texteditor:
    #function to open file
    current_open_file="No file"#it is used to check whether a new file is created or previous is opened
    def open_file(self):
        open_return=filedialog.askopenfile(initialdir="/home/prem/Desktop/summer/",title="Select file",filetypes=(("Text Files",".txt"),("All files","*")))
        if (open_return) is not None:
            self.text_area.delete(1.0,END)#This is done to delete content of previously loaded file from textbox
            for file in open_return:
                self.text_area.insert(END,file)
            self.current_open_file=open_return.name
        open_return.close()
    
    #function for save as file
    def saveas(self):
        f=filedialog.asksaveasfile(mode="w",defaultextension=".txt") 
        if f is None:
            return
        text2save=self.text_area.get(1.0,END)
        self.current_open_file=f.name
        f.write(text2save)
        f.close
    #function to save file
    def savefile(self):
        if self.current_open_file =="No file":
            self.saveas()
        else:
            f=open(self.current_open_file,"w+")
            f.write(self.text_area.get(1.0,END))
    #function to open new file
    def newfile(self):
        self.text_area.delete(1.0,END)
        self.current_open_file="No file"
    def copy(self):
        self.text_area.clipboard_clear()
        ll=self.text_area.clipboard_append(self.text_area.selection_get())
    def cut(self):
        self.copy()
        self.text_area.delete("sel.first","sel.last")
        #index of first selected text is in sel.first and last index of selected text is in sel.last
    def paste(self):
        self.text_area.insert(INSERT,self.text_area.clipboard_get())#INSERT shows the current position of cursor
        
    
    #Function to create menu bars
    def __init__(self,master):
        self.master=master
        master.title("Text Editor")
        self.text_area=Text(self.master,undo=True)
        self.text_area.pack(fill=BOTH,expand=1)#fill is used to make text box of the size of start but this workds only in x axis
        #so expand=1 is used to make it expandable textbox along with start
        self.mainmenu=Menu(self.master)
        self.master.config(menu=self.mainmenu)
        #creating file menu & tearoff is used to remove dashed line in starting
        self.filemenu=Menu(self.mainmenu,tearoff=False)
        self.mainmenu.add_cascade(label="File",menu=self.filemenu)
        self.filemenu.add_command(label="New",command=self.newfile)
        self.filemenu.add_command(label="Open",command=self.open_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Save",command=self.savefile)
        self.filemenu.add_command(label="Save as",command=self.saveas)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=master.quit)
        #creating edit
        self.editmenu=Menu(self.mainmenu,tearoff=False)
        self.mainmenu.add_cascade(label="Edit",menu=self.editmenu)
        self.editmenu.add_command(label="Cut",command=self.cut)
        self.editmenu.add_command(label="Copy",command=self.copy)
        self.editmenu.add_command(label="Paste",command=self.paste)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Undo",command=self.text_area.edit_undo)
        self.editmenu.add_command(label="Redo",command=self.text_area.edit_redo)
        
        
        
        
te=texteditor(start)#creating object of class
start.geometry("300x300")
start.mainloop()
