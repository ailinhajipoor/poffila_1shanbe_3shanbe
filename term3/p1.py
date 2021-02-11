from tkinter import *
root=Tk()
#text=متن
root.configure(bg="orange")  #bg  ->   background  پس زمینه
l1=Label(root,text="name !")
l1.pack()
e1=Entry(root)
e1.pack()
l1=Label(root,text="last name !")
l1.pack()
e1=Entry(root)
e1.pack()
l1=Label(root,text="age !")
l1.pack()
e1=Entry(root)
e1.pack()

root.mainloop()