import tkinter
from tkinter.simpledialog import askinteger
from tkinter import messagebox


def sor():
    num = askinteger("Input", "Input an Integer")
    print(num)
    
pencere = tkinter.Tk()
dugme = tkinter.Button(pencere,text="sayi gir")
dugme.pack()
dugme["command"] = sor
pencere.mainloop()
