from tkinter import *

pencere = Tk()

kutu = Frame(pencere).pack()
kutu1 = Frame(pencere).pack(side = BOTTOM)
kutu2 = Frame(pencere).pack(side = BOTTOM)

kbutton = Button(kutu, text="Kırmızı", fg="red").pack(side=LEFT)
tbutton = Button(kutu, text="Yeşil", fg="green").pack(side=LEFT)
mbutton = Button(kutu, text="Mavi", fg="blue").pack(side=TOP)

sbutton = Button(kutu1, text="Siyah", fg="black").pack(side=BOTTOM)

bbutton = Button(kutu2, text="Beyaz", fg="white").pack(side=RIGHT)

pencere.mainloop()
