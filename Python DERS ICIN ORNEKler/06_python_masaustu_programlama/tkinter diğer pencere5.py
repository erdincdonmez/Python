import tkinter as tk

def ana_ekran():
    anaekran = tk.Tk()
    anaekran.geometry("200x200+200+100")
    button = tk.Button(anaekran, text="Şİfre gir")
    button['command'] = sifre_ekrani
    button.pack()
    anaekran.mainloop()

def sifre_ekrani():
    try:
        if login.state() == "normal": login.focus()
    except NameError as e:
        print(e)
        login = tk.Toplevel()
        login.geometry("300x150+500+200")
        login["bg"] = "navy"
        lb = tk.Label(login, text="Hello")
        lb.pack()
        button = tk.Button(login, text="Tamam")
        button['command'] = lambda:login.withdraw()
        button.pack()

ana_ekran()

