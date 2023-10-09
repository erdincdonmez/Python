import tkinter as tk


#login.deiconify()

def ana_ekran():
    anaekran = tk.Tk()
    #login.withdraw()
    anaekran.geometry("200x200+200+100")
    button = tk.Button(anaekran, text="Şifre sor").pack()
    button['command'] = sifre_ekrani
    button.pack()
    anaekran.mainloop()
    
def sifre_ekrani():
    login = tk.Toplevel()
    #login.withdraw()
    try:
        if login.state() == "normal": login.focus()
    except NameError as e:
        print(e)
        login.geometry("300x300+500+200")
        login["bg"] = "navy"
        lb = tk.Label(login, text="Kullanıcı adı ve şifre girişi")
        lb.pack()
        button = tk.Button(login, text="Ana ekrana dön")
        button.pack()

ana_ekran()

