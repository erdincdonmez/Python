import tkinter as tk

class Gui:
    """Gui class"""
    def __init__(self):
        self.root = tk.Tk()

        self.new_window = tk.Button(master=self.root, text="Pencere aç", command=self.new_window)
        self.new_window.pack()
        self.root.mainloop()

    def new_window(self):
        """Create a new top level window"""
        new_window = tk.Toplevel()
        tk.Label(master=new_window, text="Yeni pencere açıldı").pack()

if __name__ == '__main__':
    Gui()
