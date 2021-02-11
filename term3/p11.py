from tkinter import *
def jam():
    number1=int(e1.get())
    number2=int(e2.get())
    print(number1+number2)

root = Tk()
root.geometry("400x300")
root.configure(bg="orange")

l1 = Label(root, text="number 1",bg="orange")
e1 = Entry(root)
l2 = Label(root, text="number 2",bg="orange")
e2 = Entry(root)

b1 = Button(root, text="+", command=jam)
b2 = Button(root, text=" -")
b3 = Button(root, text=" *")
b4 = Button(root, text=" /")

l1.grid(row=0, column=0, padx=50, pady=10)
e1.grid(row=0, column=1, pady=10)
l2.grid(row=1, column=0, pady=10)
e2.grid(row=1, column=1, pady=10)
b1.grid(row=2, column=0, pady=10)
b2.grid(row=2, column=1, pady=10)
b3.grid(row=3, column=0, pady=10)
b4.grid(row=3, column=1,pady=10)

root.mainloop()
