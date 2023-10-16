from tkinter import *
top = Tk()

#entry_text = top.StringVar()
#entry = top.Entry(root, textvariable=entry_text)

def topla():
    total = E1 + E2
    e.delete(0,END)
    E3.insert(0,total)
    #entry_text.set("xx")
    print(E3)


L1 = Label(top, text="1.Sınav").place(x=10,y=10)
E1 = Entry(top, bd =5).place(x=60,y=10)
L2=Label(top,text="2.Sınav").place(x=10,y=50)
E2=Entry(top,bd=5).place(x=60,y=50)



L3=Label(top,text="Sonuc").place(x=10,y=150)
E3=Entry(top,bd=5).place(x=60,y=150)
B = Button(top, text ="Ortalaması", command="topla()").place(x=100, y=100)
top.geometry("250x250+10+10")
top.mainloop()




