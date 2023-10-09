#Python Label Kullanımı
from tkinter import *
from tkinter import messagebox
pencere = Tk()
pencere.title("erdincdonmez.com")
pencere.geometry("400x200")
#formu grid olarak çizdirme /layout düzeni
uygulama = Frame(pencere)
uygulama.grid()
 
#label nesnesini çiz
etiket = Label(uygulama,text="Kullanıcı adı: ")
etiket.grid(column=2, row=2)

# etiket.grid(padx=2, pady=0)
etiket2 = Label(uygulama,text="Şifre :").grid(column=2, row=1)
 
#formu çiz
pencere.mainloop()
