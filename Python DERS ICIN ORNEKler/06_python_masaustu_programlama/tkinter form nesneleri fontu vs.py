from tkinter import *
win= Tk() #Create an instance of tkinter frame or window
win.geometry("250x180")

mytext = "Fontlu label"
Label(win, text="Fontsuz label",bg='#000', fg='#ff0', padx=9, pady=5).pack()
Label(win, text="Fontsuz label",bg='#f00', fg='#fff').pack(pady=20)
Label(win, text=mytext, font= ('Helvetica 20 bold')).pack()
Button(win, text='Stop', font= ('Helvetica 15 bold')).pack()
win.mainloop()
