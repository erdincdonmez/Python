from tkinter import *
def cevir():
    print(girilen.get())
form = Tk()

form2 = Tk()


girilen = Entry()
girilen.place(x=20,y=10)
Button(text="Çevir",pady=5,padx=5,command=cevir).place(x=20,y=40)
Label(form, text='inch karşılığı').place(x=20,y=75)
Label(form, text='cm karşılığı').place(x=20,y=90)

Label(form2, text='inch karşılığı').place(x=20,y=75)
Label(form2, text='cm karşılığı').place(x=20,y=90)

form.mainloop()
