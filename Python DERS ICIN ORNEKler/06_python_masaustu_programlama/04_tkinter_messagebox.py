#Python Tkinter butona basınca mesaj gösterme
from tkinter import *
 
from tkinter import messagebox
 
pencere = Tk()
 
pencere.title("erdincdonmez.com")
pencere.geometry("400x300")
 
uygulama = Frame(pencere)
uygulama.grid()
 
#mesaj fonksiyonu
def dialog():
    var = messagebox.showinfo("Uyarı" , "bu bir messagebox")
 
#buton nesnesini çiz ve fonksiyonu bağla
button1 = Button(uygulama, text = " Uyarı Ver " , width=20, command=dialog) # dialog() şeklinde kullanırsanız otomatik çağırılır.
button1.grid(padx=110, pady=70)
 
#label nesnesini çiz
etiket = Label(uygulama,text="messagebox açmak için düğmeye tıklayın")
etiket.grid(padx=110, pady=10)
 
#formu çiz
pencere.mainloop()
