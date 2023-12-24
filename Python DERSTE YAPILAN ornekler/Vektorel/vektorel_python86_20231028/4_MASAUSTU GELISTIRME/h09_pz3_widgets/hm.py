from PyQt5.QtWidgets import *
import sys
import Hesap_Makinesi
import math
from PyQt5.QtGui import *
from PyQt5.QtCore import *







class Pencere(QMainWindow, Hesap_Makinesi.HesapMakinesi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer()
        
        self.pushButton.clicked.connect(self.click1)
        self.pushButton_2.clicked.connect(self.click2)
        self.pushButton_3.clicked.connect(self.click3)
        self.pushButton_4.clicked.connect(self.click4)
        self.pushButton_5.clicked.connect(self.click5)
        self.pushButton_6.clicked.connect(self.click6)
        self.pushButton_7.clicked.connect(self.click7)
        self.pushButton_8.clicked.connect(self.click8)
        self.pushButton_9.clicked.connect(self.click9)
        self.pushButton_10.clicked.connect(self.click10)
        self.pushButton_12.clicked.connect(self.click11)
        self.pushButton_17.clicked.connect(self.click12)
        self.pushButton_14.clicked.connect(self.click13)
        self.pushButton_15.clicked.connect(self.click14)
        self.pushButton_11.clicked.connect(self.click15)
        self.pushButton_13.clicked.connect(self.click16)
        self.pushButton_16.clicked.connect(self.click17)
        self.pushButton_16.setContextMenuPolicy(Qt.CustomContextMenu)
        self.pushButton_16.customContextMenuRequested.connect(self.handle_right_click)
        
        
        
        
        

        self.pushButton_18.clicked.connect(self.clicklast)
        self.pushButton_19.clicked.connect(self.delete)
        self.pushButton_20.clicked.connect(self.karekok)
        
        
        
            

        
        
    

    def click1(self):
        
        yazi = self.lineEdit.text() + "1"
        self.lineEdit.setText(yazi)

    def click2(self):
        yazi = self.lineEdit.text() + "2"
        self.lineEdit.setText(yazi)

    def click3(self):
        yazi = self.lineEdit.text() + "3"
        self.lineEdit.setText(yazi)

    def click4(self):
        yazi = self.lineEdit.text() + "4"
        self.lineEdit.setText(yazi)

    def click5(self):
        yazi = self.lineEdit.text() + "5"
        self.lineEdit.setText(yazi)

    def click6(self):
        yazi = self.lineEdit.text() + "6"
        self.lineEdit.setText(yazi)

    def click7(self):
        yazi = self.lineEdit.text() + "7"
        self.lineEdit.setText(yazi)
    
    def click8(self):
        yazi = self.lineEdit.text() + "8"
        self.lineEdit.setText(yazi)

    def click9(self):
        yazi = self.lineEdit.text() + "9"
        self.lineEdit.setText(yazi)

    def click10(self):
        yazi = self.lineEdit.text() + "0"
        self.lineEdit.setText(yazi)

    def click11(self):
        self.lineEdit.clear()

    def click12(self):
        superscript = {
    "0": "\u2070",
    "1": "\u00b9",
    "2": "\u00b2",
    "3": "\u00b3",
    "4": "\u2074",
    "5": "\u2075",
    "6": "\u2076",
    "7": "\u2077",
    "8": "\u2078",
    "9": "\u2079"
}


        def get_superscript(x):
            return "".join(superscript[i] for i in str(x))
    

        def exponential_expression(x):
            count = 2
            while (y := math.log(x, count)) != int(y):
                count += 1
            return f"{count}{get_superscript(int(y))}"
        
        try:
            
            d = self.lineEdit.text()
            self.lineEdit.setText(exponential_expression(x=int(d)))
            
        except ValueError:
            self.lineEdit.setText("Geçersiz İşlem")
            
        
        self.label_2.setText(self.lineEdit.text())

        

    def click13(self):
        yazi = self.lineEdit.text() + "+"
        self.lineEdit.setText(yazi)

    def click14(self):
        yazi = self.lineEdit.text() + "-"
        self.lineEdit.setText(yazi)

    def click15(self):
        yazi = self.lineEdit.text() + "*"
        self.lineEdit.setText(yazi)

    def click16(self):
        yazi = self.lineEdit.text() + "/"
        self.lineEdit.setText(yazi)
        

    def click17(self):
        yazi = self.lineEdit.text() + "**"
        self.lineEdit.setText(yazi)
        
        
        
    def handle_right_click(self):
        
        yazi = self.lineEdit.text() + "."
        self.lineEdit.setText(yazi)
        
        
        
    def delete(self):
        text = self.lineEdit.text()
        print(text[:len(text)-1]) 
        self.lineEdit.setText(text[:len(text)-1]) 
        
        
        
    def karekok(self):
        try:
            self.label_2.setText(self.lineEdit.text())
            txt = self.lineEdit.text()
            integer = int(txt)   
            rp = int(math.sqrt(abs(integer)))     
        
        
            ans = eval("{}*{}".format(str(rp),str(rp)))
        
            if str(ans) == self.label_2.text():
                self.lineEdit.setText(str(rp)+"^2") 
            
            
            else:         
                self.lineEdit.setText("Bu Sayının Karekökü Yoktur")
            
        except ValueError:
            self.lineEdit.setText("Geçersiz İşlem")
            

    
    def clicklast(self):
        # get the label text 
        equation = self.lineEdit.text() 
  
        try: 
            # getting the ans 
            ans = eval(equation) 
  
            # setting text to the label 
            self.lineEdit.setText(str(ans)) 
  
        except: 
            # setting text to the label 
            self.lineEdit.setText("Geçersiz İşlem")
            
        
        self.label_2.setText(self.lineEdit.text())
        
        
        
app = QApplication(sys.argv)
pencere = Pencere()
pencere.setWindowTitle("Hesap Makinesi")
pencere.show()
sys.exit(app.exec_())