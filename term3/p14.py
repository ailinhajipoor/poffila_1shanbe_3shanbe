from tkinter import *
from tkinter.ttk import Combobox

def save_to_file():
    print(c1.get())
    print(e1.get())
    f=open("info.txt", "a")
    f.write(c1.get())
    f.write("\n")
    f.write(e1.get())
    f.write("\n")
    f.close()

root=Tk()
root.geometry("200x200")
c1=Combobox(root,value=["شنبه","یکشنبه","دوشنبه","سه شنبه","چهارشنبه"])
c1.set("choose one ...")
l1=Label(root,text= "name")
e1=Entry(root)
b1=Button(root,text="Save",command=save_to_file)

c1.pack()
l1.pack()
e1.pack()
b1.pack()

root.mainloop()