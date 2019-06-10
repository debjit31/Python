#to count the number of times a button is clicked

import tkinter
count=0
root = tkinter.Tk()
root.title("Counter")
root.geometry("600x400")
root.resizable(0,0)
root.configure(background="lightblue")

def fun():
    global count
    count+=1
    label1=tkinter.Label(root,text="You have clicked "+str(count),fg="navy")
    label1.grid(row=1,column=0,padx=20,pady=20)

button1=tkinter.Button(root,text="CLICK HERE",bd="10",fg="navy",command=fun)
button1.grid(row=0,column=0,padx=20,pady=30)
