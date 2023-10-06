import tkinter as tk
 
def tiklandi():
    num1 = int(edit1.get())
    buton1.config(text="Bana tıklandı"+str(num1))
def xxx():
    #label1.config(text=buton1.cget('text'))
    label1.config(text=edit1.get())
 
# create the main window
root = tk.Tk()
root.title("Butonlara tıklanınca fonksiyon çalıştır")
 
# create the widgets
edit1 = tk.Entry(root)
buton1 = tk.Button(root, text="Tıkla", command=tiklandi)
buton2 = tk.Button(root, text="label değiştir", command=lambda:label1.config(text="label içi değişti"))
buton3 = tk.Button(root, text="yazıyı labela aktar", command=xxx)
label1 = tk.Label(root, text="Label")
 
# layout the widgets
edit1.grid(row=0, column=0, padx=10, pady=10)
buton1.grid(row=2, column=0, columnspan=2, pady=10)
buton2.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
buton3.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
label1.grid(row=3, column=0, columnspan=2, pady=10)
 
# run the main loop
root.mainloop()
