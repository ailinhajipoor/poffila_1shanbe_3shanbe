from tkinter import  *
def iran():
    l1.configure(bg="green")
    l2.configure(bg="white",text="God")
    l3.configure(bg="red")
def italy():
    l1.configure(bg="red")
    l2.configure(bg="white",text=" ")
    l3.configure(bg="green")
root=Tk()
root.geometry("400x300")
root.configure(bg="white")
b1=Button(root,text="iran",width=10,command=iran)
b2=Button(root,text="italy",width=10,command=italy)
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
f=Frame(root)
f.grid(row=1,column=0)

l1=Label(f,height=4)
l2=Label(f,height=4)
l3=Label(f,height=4)

l1.pack(fill="both")
l2.pack(fill="both")
l3.pack(fill="both")
root.mainloop()