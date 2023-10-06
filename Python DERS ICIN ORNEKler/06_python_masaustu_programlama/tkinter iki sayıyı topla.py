import tkinter as tk
 
def topla():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result = num1 + num2
    result_label.config(text=result)
 
# create the main window
pencere = tk.Tk()
pencere.title("İki sayıyı topla")
 
# create the widgets
num1_label = tk.Label(pencere, text="Sayı 1:")
num1_entry = tk.Entry(pencere)
num2_label = tk.Label(pencere, text="Sayı 2:")
num2_entry = tk.Entry(pencere)
add_button = tk.Button(pencere, text="Topla", command=topla)
result_label = tk.Label(pencere, text="Sonuc:")
 
# layout the widgets
num1_label.grid(row=0, column=0, sticky="e")
num1_entry.grid(row=0, column=1)
num2_label.grid(row=1, column=0, sticky="e")
num2_entry.grid(row=1, column=1)
add_button.grid(row=2, column=0, columnspan=2, pady=10)
result_label.grid(row=3, column=0, columnspan=2)
 
pencere.mainloop()
