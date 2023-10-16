#Tkinter ListBox Kullanımı
from tkinter import *
from tkinter import messagebox
def yaz():
    secim=Lb1.get()
    print(secim)
pencere = Tk()
pencere.title("erdincdonmez.com")
pencere.geometry("400x300")

uygulama = Frame(pencere) # grid form çizdirme
uygulama.grid()

# tkinter.ttk.Label(pencere, text="Liste")
Lb1 = Listbox(uygulama, )
Lb1.insert(1, "Python")
Lb1.insert(2, "C#")
Lb1.insert(3, "JAVA")
Lb1.insert(4, "JAVASCRIPT")
Lb1.grid(padx=110, pady=10)
 

pencere.mainloop()#formu çiz
