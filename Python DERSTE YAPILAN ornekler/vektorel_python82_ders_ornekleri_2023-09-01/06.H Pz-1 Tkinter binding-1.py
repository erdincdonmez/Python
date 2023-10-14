from tkinter import *
win= Tk()
win.geometry("700x350")

def tiklama(e):
   label.config(text="Fare tuşuna tıklandı", font=('Helvetica 17 bold'))

def basma(e):
   label.config(text="Bir tuşa basıldı", font=('Helvetica 17 bold'))

def basma_a(e):
   label.config(text="a tuşuna basıldı", font=('Helvetica 17 bold'))

def basma_k(e):
   label.config(bg="red")

def mavi(e):
   win.config(bg="blue")

def xxxx(e):
    label.config(bg="olive")

label = Label(win, text= "x")
label.pack(pady= 50)

# Bind the Mouse button event
win.bind('<Button-1>',tiklama)
# win.bind('<KeyRelease>',basma)
win.bind('a',basma_a)
win.bind('k',basma_k)
win.bind('m',mavi)
win.bind('h',xxxx)
win.mainloop()
