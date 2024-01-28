import tkinter as tk 
r = tk.Tk()

r.title('Counting Seconds') 

button = tk.Button(r, text='Stop', width=25, height=5, command=r.destroy) 
button.pack()
button1 = tk.Button(r, text='Stop', width=125, command=r.destroy) 
button1.pack() 
r.mainloop() 
