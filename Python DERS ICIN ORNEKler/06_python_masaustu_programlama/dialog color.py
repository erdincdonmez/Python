from tkinter.colorchooser import askcolor
from tkinter import *

top = Tk()

top.geometry("100x100")
def show():
   color = askcolor()
   print(color)
   
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)

top.mainloop()

