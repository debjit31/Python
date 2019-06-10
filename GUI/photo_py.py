import tkinter

window = tkinter.Tk()
window.title("Image")
window.geometry("600x400")
p=tkinter.PhotoImage(file="download.png")
lbl=tkinter.Label(tk,image=p)
lbl.image = p
lbl.place(x=0,y=0,relwidth= 1, relheight = 1)

b=tkinter.Button(window,text = "hello").grid(row=0,column=0,padx=20,pady=30)
 
