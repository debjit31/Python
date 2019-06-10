##from tkinter import *
##
##root = Tk()
##
##def printname():
##    print("Hello gui user")
##button1=Button(root,text="Print",command=printname)
##button1.pack()
##
##root.mainloop()







from tkinter import *

root = Tk()

def printname(event):
    print("Hello gui user")
button1=Button(root,text="Print")
button1.bind("<Button-1>",printname)
button1.pack()

root.mainloop()







