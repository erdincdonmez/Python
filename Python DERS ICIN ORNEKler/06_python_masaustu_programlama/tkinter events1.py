# Import the Required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win= Tk()

# Set the size of the window
win.geometry("700x350")

# Define a function to display the message
def display_text(e):
   label.config(text="Code never lies, comments sometimes do", font=('Helvetica 17 bold'))

# Create a label widget to add some text
label= Label(win, text= "")
label.pack(pady= 50)

# Bind the Mouse button event
win.bind('<Button-1>',display_text)
win.mainloop()
