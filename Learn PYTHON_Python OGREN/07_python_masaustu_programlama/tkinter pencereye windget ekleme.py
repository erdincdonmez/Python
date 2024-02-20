from tkinter import *
pencere= Tk()

xxx = "Değişkendeki"
Label(text="Label1").pack()
Label(text=xxx).pack()
Button(text='Stop').pack(anchor = W)
Checkbutton(text=xxx).pack()
Entry(text="bu bir entry").pack()
Checkbutton(text=xxx).pack()
Text(height=7,width=30).pack()
Radiobutton(text="radio button",value = 0).pack()
Radiobutton(text=xxx,value = 1).pack(anchor = W)
Scale().pack()
Scrollbar().pack()
Spinbox().pack()
pencere.mainloop()


