#login format
import tkinter
window = tkinter.Tk()
window.title("Login")
window.geometry("600x400")
window.resizable(0,0)
window.configure(background="light blue")

#------------------------------------Registration Form-------------------------

def show():
    rgwindow=tkinter.Tk()
    rgwindow.title("Sign Up")
    rgwindow.geometry("600x400")
    rgwindow.resizable(0,0)
    rgwindow.configure(background="light blue")
    #----------------------------NAME_-------------------------------


    label0=tkinter.Label(rgwindow,text="Name :- ",font=("Arial",10,"bold"),bd="10",fg="navy")
    label0.grid(row=0,column=0,padx=20,pady=20)

    entry00=tkinter.Entry(rgwindow,fg="navy")   
    entry00.grid(row=0,column=1,padx=10,pady=20)

  
    #----------------------------USER NAME_-------------------------------


    label11=tkinter.Label(rgwindow,text="User Name :- ",font=("Arial",10,"bold"),bd="10",fg="navy")
    label11.grid(row=1,column=0,padx=20,pady=20)

    entry11=tkinter.Entry(rgwindow,fg="navy")
    entry11.grid(row=1,column=1,padx=10,pady=20)

    #----------------------------------PASSWORD-----------------------------

    label22=tkinter.Label(rgwindow,text="Password",font=("Arial",10,"bold"),fg="navy")
    label22.grid(row=2,column=0,padx=10,pady=20)

    entry22=tkinter.Entry(rgwindow,show="*",fg="navy")
    entry22.grid(row=2,column=1,padx=10,pady=10)



    #-----------------------------Contact Number----------------------
    label22=tkinter.Label(rgwindow,text="Contact Number",font=("Arial",10,"bold"),fg="navy")
    label22.grid(row=3,column=0,padx=10,pady=20)

    entry22=tkinter.Entry(rgwindow,fg="navy")
    entry22.grid(row=3,column=1,padx=10,pady=10)



#------------------------------LOGIN FORM----------------------------
#----------------------------USER NAME_-------------------------------


label1=tkinter.Label(window,text="User Name :- ",font=("Arial",10,"bold"),bd="10",fg="navy")
label1.grid(row=0,column=0,padx=20,pady=20)

entry1=tkinter.Entry(window,fg="navy",bd="10")
entry1.grid(row=0,column=1,padx=10,pady=20)

#----------------------------------PASSWORD-----------------------------

label2=tkinter.Label(window,text="Password",font=("Arial",10,"bold"),fg="navy")
label2.grid(row=1,column=0,padx=10,pady=20)

entry2=tkinter.Entry(window,show="*",fg="navy",bd="10")
entry2.grid(row=1,column=1,padx=10,pady=10)
#-----------------------------------------LOGIN------------------------------

button1=tkinter.Button(window,text="Login",fg="black")
button1.grid(row=2,column=0,columnspan=2)

button2=tkinter.Button(window,text="Register",fg="black",command=show)
button2.grid(row=2,column=3,columnspan=2)
