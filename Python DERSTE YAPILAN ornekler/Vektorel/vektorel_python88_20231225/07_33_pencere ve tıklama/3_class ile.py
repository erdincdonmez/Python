from PyQt6.QtWidgets import *

class Pencere (QMainWindow):
    pass

uygulama = QApplication([])

anapencere = Pencere()
anapencere.setWindowTitle('Deneme')
anapencere.resize(300,50)
anapencere.show()

uygulama.exec() # Bunu yazmadan deneyin, bakalım ne olacak.

