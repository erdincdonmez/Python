import tkinter as tk
 
def cevir():
    
    
    

    if num1_entry.get()!="":
        num1 = float(num1_entry.get())
        result = num1 * 2.54
        inch = "inch karşılığı:" + str(result)
        cm = "cm karşılığı:" + str(num1)
        result_label.config(text=inch)
        result_label1.config(text=cm)
        print(result)
        
    if num1_entry1.get()!="":
        num2 = float(num1_entry1.get())
        result = num2 / 2
        inch = "inch karşılığı:" + str(num2)
        cm = "cm karşılığı:" + str(result)
        result_label.config(text=inch)
        result_label1.config(text=cm)
        print(result)    
 
# pencereyi oluştur
pencere = tk.Tk()
pencere.title("İki sayıyı topla")
 
# araçları ekle
num1_label = tk.Label(pencere, text="cm gir:")
num1_entry = tk.Entry(pencere)

num1_label1 = tk.Label(pencere, text="inch gir:")
num1_entry1 = tk.Entry(pencere)

add_button = tk.Button(pencere, text="Çevir", command=cevir)
result_label = tk.Label(pencere, text="inch karşılığı:")
result_label1 = tk.Label(pencere, text="cm karşılığı:")
 
# araçları yerleştir
num1_label.grid(row=0, column=0, sticky="e")
num1_entry.grid(row=0, column=1)
num1_label1.grid(row=1, column=0, sticky="e")
num1_entry1.grid(row=1, column=1)
add_button.grid(row=2, column=0, columnspan=2, pady=10)
result_label.grid(row=3, column=0, columnspan=2)
result_label1.grid(row=4, column=0, columnspan=2)
 
pencere.mainloop()
