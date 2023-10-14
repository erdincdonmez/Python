import tkinter
def yaz():
    print("Tıklandı")
def sagTik(xx):
    print("Butonda Sağ tıklandı")
def sagTik1(xx):
    print("Formda Sağ tıklandı")
def tusAbasildi(xx):
    print("Formda a tuşuna basıldı")
    form.title("A tuşuna basıldı")
    form.config(bg="red")
def xxx(xx):
    print("Formda S tuşuna basıldı")
    form.title("S tuşuna basıldı")
    form.config(bg="green")
form = tkinter.Tk()
form.geometry("300x300")
 
label1 = tkinter.Label(form, text="Label")
buton1 = tkinter.Button(form, text="Tıkla", command=yaz)

label1.grid(row=1, column=1, pady=10)
buton1.grid(row=1, column=0, padx=10)

buton1.bind("<Button-3>",sagTik)
form.bind("<Button-3>",sagTik1)
form.bind("<Button-3>",sagTik1)
form.bind("a",tusAbasildi)
form.bind("s",xxx)

form.mainloop()

