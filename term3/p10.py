from tkinter import *

def havij():
    print(e1.get())
    print(e2.get())
    print(e3.get())

root = Tk()
root.geometry("400x300")
root.configure(bg="orange")

l1 = Label(root, text="name")
e1 = Entry(root)
l2 = Label(root, text="last name")
e2 = Entry(root)
l3 = Label(root, text="age")
e3 = Entry(root)

b1 = Button(root, text="Ok", command=havij)
b2 = Button(root, text="Clear")

l1.grid(row=0, column=0, padx=30, pady=10)
e1.grid(row=0, column=1, pady=10)
l2.grid(row=1, column=0, pady=10)
e2.grid(row=1, column=1, pady=10)
l3.grid(row=2, column=0, pady=10)
e3.grid(row=2, column=1, pady=10)
b1.grid(row=3, column=0, pady=10)
b2.grid(row=3, column=1, pady=10)

root.mainloop()
