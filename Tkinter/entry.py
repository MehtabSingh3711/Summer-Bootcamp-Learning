# ENTRY WIDGET ALSO USED FOR INPUT TEXT
from tkinter import *

root = Tk()

e = Entry(root, width=50, font=('Helvetica', 24))
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello)
	e.delete(0, 'end')
	myLabel.pack()

myButton = Button(root, text="Enter", command=myClick)
myButton.pack()

root.mainloop()