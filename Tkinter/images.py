from tkinter import *
from PIL import ImageTk,Image

# Create the root window
root = Tk()
# Set the title of the root window
root.title('Mehtab')
root.iconbitmap(r"C:\Users\mehta\Downloads\visa (1).png")

# Load the image
my_img = ImageTk.PhotoImage(Image.open(r"C:\Users\mehta\Downloads\visa (1).png"))
# Create a label to display the image
my_label = Label(image=my_img)
my_label.pack()
button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()
root.mainloop()