from tkinter import *
def benevis1():
    print(e1.get())
def benevis2():
    print(e2.get())
reza=Tk()
reza.configure(bg="tomato")
l1=Label(reza,text="name",bg="tomato")
l1.pack()

e1=Entry(reza,bg="red")
e1.pack()

b1=Button(reza,text="ok",bg="yellow",fg="green",command=benevis1)
b1.pack()

l2=Label(reza,text="last name",bg="tomato")
l2.pack()

e2=Entry(reza,bg="red")
e2.pack()

b2=Button(reza,text="ok",bg="yellow",fg="green",command=benevis2)
b2.pack()

#fg  رنگ فونت
#bg رنگ پس زمینه
reza.mainloop()