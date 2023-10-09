from tkinter import *
from tkinter import ttk

win= Tk() # Create an instance of tkinter frame or window

win.geometry("750x250") # Set the geometry of tkinter frame

def open_win(): # Define a new function to open the window
   new= Toplevel(win)
   new.geometry("750x250")
   new.title("New Window") # Create a Label in New window
   Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold')).pack(pady=30) # Create a label

Label(win, text= "Yeni pencere için tıkla", font= ('Helvetica 17 bold')).pack(pady=30) 
ttk.Button(win, text="Open", command=open_win).pack()
win.mainloop()
