from tkinter import *

def print_kon():
    print(amir.get())
root=Tk()
amir=StringVar()
r1=Radiobutton(root,text="yellow",value="yellow",variable=amir)
r2=Radiobutton(root,text="red",value="red",variable=amir)
r3=Radiobutton(root,text="blue",value="blue",variable=amir)
b1=Button(root,text="print",command=print_kon)
r1.pack()
r2.pack()
r3.pack()
b1.pack()
root.mainloop()
