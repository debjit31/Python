from tkinter import *

def donothing():
    print("ok ok i wont")
   
root = Tk()

menu1 = Menu(root)
root.config(menu=menu1)

subMenu=Menu(menu1)
menu1.add_cascade(label="File",menu=Submenu)


root.mainloop()
