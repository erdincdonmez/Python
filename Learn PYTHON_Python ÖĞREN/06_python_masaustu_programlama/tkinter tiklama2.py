import tkinter

def xxx():
    label1.config(text="Tıklandı")
    
form = tkinter.Tk()
 
label1 = tkinter.Label(form, text="Label")
buton1 = tkinter.Button(form, text="Tıkla", command=xxx)

label1.grid(row=1, column=1, pady=10)
buton1.grid(row=1, column=0, padx=10)

root.mainloop()
