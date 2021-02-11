from tkinter import  *
def r():
    root.configure(bg="red")
    lf.configure(bg="red")
def b():
    root.configure(bg="blue")
    lf.configure(bg="blue")
def g():
    root.configure(bg="green")
    lf.configure(bg="green")
def fr():
    b1.configure(fg="red")
    b2.configure(fg="red")

root=Tk()
root.configure(bg="white")
root.geometry("400x500")
#width= عرض
#height=ارتفاع
lf=LabelFrame(root,text="background color" ,bg="white")
lf.pack()
lff=LabelFrame(root,text="****font color****" ,bg="white")
lff.pack()
b1=Button(lf,text="red",command=r,width=5,height=2)
b1.pack()
b2=Button(lf,text="blue",command=b,width=5,height=2)
b2.pack()
b2=Button(lf,text="green",command=g,width=5,height=2)
b2.pack()
b1=Button(lff,text="red",command=fr,width=5,height=2)
b1.pack()
b2=Button(lff,text="blue",width=5,height=2)
b2.pack()
b2=Button(lff,text="green",width=5,height=2)
b2.pack()
root.mainloop()