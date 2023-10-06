from tkinter import *
master = Tk() 
var1 = IntVar() 
Checkbutton(master, text='Türkçe', variable=var1).grid(row=0, sticky=W) 
var2 = IntVar() 
Checkbutton(master, text='Matematik', variable=var2).grid(row=1, sticky=W) 
mainloop() 
