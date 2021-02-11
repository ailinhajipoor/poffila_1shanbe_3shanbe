from tkinter import *
root=Tk()
root.geometry("300x300")
root.configure(bg="orange")
root.title("first project")#عنوان

l1=Label(root,text="welcome to our first project",bg="tomato")
l1.pack(fill="both")

l2=Label(root,text="made by poulstar group",bg="tomato")
l2.pack(side="bottom",fill="both")

root.mainloop()