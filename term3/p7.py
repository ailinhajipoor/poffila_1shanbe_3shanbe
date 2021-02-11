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
b1.pack()
b2.pack()

l1=Label(root,height=4)
l2=Label(root,height=4)
l3=Label(root,height=4)

l1.pack(fill="both")
l2.pack(fill="both")
l3.pack(fill="both")
root.mainloop()