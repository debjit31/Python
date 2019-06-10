import tkinter

window=tkinter.Tk()
window.title("hello user")
window.geometry("400x400")
window.configure(background="red")
lb1=tkinter.Label(window,text="welcome to gui",bg="green",fg="white")
lb1.pack()
#
txt=tkinter.Entry(window,bg="black",fg="white")
txt.pack()
##
def disp():
    s=txt.get()
    s='hello'+s
    lblresult.config(text=s)


b=tkinter.Button(window,text="click",bg="cyan",fg="red",command=disp)
b.pack()
##
lblresult=tkinter.Label(window,text="",bg="green",fg="white")
lblresult.pack()
