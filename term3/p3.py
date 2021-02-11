from tkinter import *
def bg_red():
    root.configure(bg="red")
    lf1.configure(bg="red")
    lf2.configure(bg="red")
def bg_orange():
    root.configure(bg="orange")
    lf1.configure(bg="orange")
    lf2.configure(bg="orange")
def bg_green():
    root.configure(bg="green")
    lf1.configure(bg="green")
    lf2.configure(bg="green")
def fg_yellow():
    b1.configure(fg="yellow")
    b2.configure(fg="yellow")
    b3.configure(fg="yellow")
    b4.configure(fg="yellow")
    b5.configure(fg="yellow")
    b6.configure(fg="yellow")
def fg_black():
    b1.configure(fg="black")
    b2.configure(fg="black")
    b3.configure(fg="black")
    b4.configure(fg="black")
    b5.configure(fg="black")
    b6.configure(fg="black")
def fg_purple():
    b1.configure(fg="purple")
    b2.configure(fg="purple")
    b3.configure(fg="purple")
    b4.configure(fg="purple")
    b5.configure(fg="purple")
    b6.configure(fg="purple")

root=Tk()
root.geometry("300x300")
root.configure(bg="white")

#---------lable frame-------------#

lf1=LabelFrame(root,text="bg color",bg="white")
lf2=LabelFrame(root,text="font color",bg="white")

#---------button  bg -------------#

b1=Button(lf1,text="red",width=5,command=bg_red)
b2=Button(lf1,text="orange",width=5,command=bg_orange)
b3=Button(lf1,text="green",width=5,command=bg_green)
#---------button  fg font -------------#
b4=Button(lf2,text="yellow",width=5,command=fg_yellow)
b5=Button(lf2,text="black",width=5,command=fg_black)
b6=Button(lf2,text="purple",width=5,command=fg_purple)

#-----------pack------------------#
lf1.pack(side="left")
lf2.pack(side="right")
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
root.mainloop()