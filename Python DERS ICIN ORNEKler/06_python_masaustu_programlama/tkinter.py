from tkinter import *

from tkinter import messagebox

pencere = Tk()

pencere.title("erdincdonmez.com")
pencere.geometry("400x300")

# grid form çizdirme
uygulama = Frame(pencere)
uygulama.grid()

L1 = Label(uygulama, text="Adınızı Girin")
L1.grid(padx=110, pady=10)

E1 = Entry(uygulama, bd=2) # bd=2 üç boyut olarak derinlik
E1.grid(padx=110, pady=3)

# formu çiz
pencere.mainloop()