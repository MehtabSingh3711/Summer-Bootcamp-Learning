from tkinter import *

root = Tk()
# Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name is Mehtab")
# GRID
myLabel1.grid(row = 0 , column =0)
myLabel2.grid(row = 0, column = 1)
root.mainloop()
