import tkinter
veri1=""
veri2=""

def yaz():
    dosya = open("rehber.txt","a")
    yazilacak = str(veri1.get())+"\n"
    dosya.write(yazilacak)
    dosya.close()
    oku()

def oku():
    dosya = open("rehber.txt","r")
    okunan = dosya.read()
    veri3.config(text=okunan)
    #veri2.config(text=okunan)
    dosya.close()

pencere = tkinter.Tk()
pencere.title("Rehber")
pencere.geometry("300x200")
button1 = tkinter.Button(pencere,text = "Dosyaya yaz", command=yaz)
button1.grid(column=1,row=1)
veri1 = tkinter.Entry()
veri1.grid(column=2,row=1)
button2 = tkinter.Button(pencere,text = "Dosyadan oku", command=oku)
button2.grid(column=1,row=2)
veri2 = tkinter.Text(height=5,width=15)
veri2.grid(column=2,row=2)
veri3 = tkinter.Label(text="okunacak veri veri")
veri3.grid(column=2,row=3)
pencere.mainloop()
