from tkinter import *
win= Tk() #Create an instance of tkinter frame or window
win.geometry("250x150")

mytext = "Fontlu label"
Label(win, text="Fontsuz label", ).pack(pady=20)
Label(win, text=mytext, font= ('Helvetica 20 bold')).pack()
Button(win, text='Stop', font= ('Helvetica 15 bold')).pack()
win.mainloop()
