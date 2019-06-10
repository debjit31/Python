from tkinter import *
root = Tk()

topframe=Frame(root)
topframe.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1=Button(topframe,text="Button_1",fg="red",bg="black")
button2=Button(topframe,text="Button_2",fg="green",bg="black")
button3=Button(topframe,text="Button_3",fg="blue",bg="black")
button4=Button(bottomFrame,text="Button_4",fg="white",bg="black")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()
