from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
top = Tk()

top.geometry("200x100")
def show():
   num = askinteger("Veri girişi", "Bir sayı giriniz: ")
   print(num)
   
B = Button(top, text ="Sayi gir", command = show)
B.place(x=50,y=50)

top.mainloop()
