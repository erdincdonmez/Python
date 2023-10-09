import tkinter as tk
yetki = "yetki yok"
ka = ""
sf = ""
def ana_ekran():
    anaekran = tk.Tk()
    anaekran.geometry("200x200")

    OgrenciNoLabel = tk.Label(anaekran,text="Öğrenci no gir")
    OgrenciNoLabel.grid(row=1,column=1)
    OgrenciNoEntry = tk.Entry(anaekran)
    OgrenciNoEntry.grid(row=1,column=2)

    print(yetki)
    if yetki == "yetki yok" : sifre_ekrani
    
    button = tk.Button(anaekran, text="Şifre gir", command=sifre_ekrani)
    button.grid(row=2,column=1)


    YetkiLabel = tk.Label(anaekran,text=yetki)
    YetkiLabel.grid(row=3,column=1) 


    
    anaekran.mainloop() # ana ekranı çalıştır.

def sifre_ekrani():
    
    def kontrol():
        print("kontrol")
        ka = enka.get()
        sf = ensf.get()
        print(ka,sf)
        if ka=="adm" and sf=="123" :
            yetki = "yetki var"
            print(yetki)
            login.withdraw()
        else:
            lbdurum.config(text="Şifre yanlış.")      
        
    try:
        if login.state() == "normal": login.focus()
    except NameError as e:
        print(e)
        login = tk.Toplevel()
        login.geometry("200x100")
        #login["bg"] = "navy"
        lbka = tk.Label(login, text="Kullanıcı adınız:")
        lbka.grid(row=1,column=1)
        enka = tk.Entry(login)
        enka.grid(row=1,column=2)
        
        
        lbsf = tk.Label(login, text="Şifreniz")
        lbsf.grid(row=2,column=1)
        ensf = tk.Entry(login)
        ensf.grid(row=2,column=2)
        
        print(ka,sf)
        button = tk.Button(login, text="Tamam")
        button['command'] = kontrol
        button.grid(row=3,column=2)

        lbdurum = tk.Label(login, text="Şifrenizi giriniz")
        lbdurum.grid(row=4,column=1)

ana_ekran()
