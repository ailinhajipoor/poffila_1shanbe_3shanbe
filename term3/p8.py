from tkinter import *
root=Tk()
root.geometry("300x300")
root.configure(bg="deeppink")

b1=Button(root,text="1")
b2=Button(root,text="2")
b3=Button(root,text="3")
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
root.minloop()