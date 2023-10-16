# Buton Oluşturma
# Burada command=exit olay tetikleyicisi oluyor.
from tkinter import *
from tkinter import messagebox
pencere = Tk()
pencere.title("erdincdonmez.com")
pencere.geometry("600x300")
uygulama = Frame(pencere)
uygulama.grid()

#button ekleme bölümü
button1 = Button(uygulama, text = " KAPAT " , width=50,height=5, command=exit)
button1.grid(padx=110, pady=80)
pencere.mainloop()

