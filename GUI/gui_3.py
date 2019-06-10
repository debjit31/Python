from tkinter import *

root=Tk()

label=Label(root,text="One",bg="red",fg="black")
label.pack()
label2=Label(root,text="Two",bg="green",fg="yellow")
label2.pack(fill=X)
label3=Label(root,text="three",bg="indigo",fg="white")
label3.pack(side=LEFT,fill=Y)

root.mainloop()
