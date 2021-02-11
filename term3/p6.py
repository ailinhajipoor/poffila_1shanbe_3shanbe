from tkinter import *
root=Tk()
root.geometry("500x300")
img=PhotoImage(file="unnamed.png")
l1=Label(root,bg="green",height=10)
l2=Label(root,image=img,bg="white")
l3=Label(root,bg="red",height=10)
l1.pack(fill="both")
l2.pack(fill="both")
l3.pack(fill="both")


root.mainloop()