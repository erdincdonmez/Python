from tkinter import *

win= Tk()
win.geometry("700x350")

def tiklama(e):
   label.config(text="Fare tuşuna tıklandı", font=('Helvetica 17 bold'))
   
def labeltiklama(e):
   label.config(text="Fare ile labele tıklandı", font=('Helvetica 17 bold'))

def basma(e):
   label.config(text="Bir tuşa basıldı", font=('Helvetica 17 bold'))

label= Label(win, text= "")
label.pack(pady= 50)

# Bind the Mouse button event
# win.bind('<Button-1>',tiklama)
win.bind('<KeyRelease>',basma)
label.bind('<Button>',labeltiklama)
win.mainloop()
