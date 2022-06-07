from PyQt5 import QtWidgets, uic
import sys
import random

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi("tictac.ui", self) # Load the .ui file

        self.lb = self.findChild(QtWidgets.QPushButton, 'label')

        self.p1.clicked.connect(self.pp1)
        self.p2.clicked.connect(self.pp2)
        self.p3.clicked.connect(self.pp3)
        self.p4.clicked.connect(self.pp4)
        self.p5.clicked.connect(self.pp5)
        self.p6.clicked.connect(self.pp6)
        self.p7.clicked.connect(self.pp7)
        self.p8.clicked.connect(self.pp8)
        self.p9.clicked.connect(self.pp9)

        self.show()

    test = ""
    def pp1(self):
        global test
        test += "a"
        x = random.randint(0, 9)
        self.p1.setText(str(x))
        self.label.setText(text)

    def pp2(self):
        global test
        test += "b"
        x = random.randint(0, 9)
        self.p2.setText(str(x))
        self.label.setText(test)

    def pp3(self):
        global test
        test += "c"
        x = random.randint(0, 9)
        self.p3.setText(str(x))
        self.label.setText(test)

    def pp4(self):
        global test
        test += "d"
        x = random.randint(0, 9)
        self.p4.setText(str(x))
        self.label.setText(test)

    def pp5(self):
        global test
        test += "e"
        x = random.randint(0, 9)
        self.p5.setText(str(x))
        self.label.setText(test)

    def pp6(self):
        global test
        test += "f"
        x = random.randint(0, 9)
        self.p6.setText(str(x))
        self.label.setText(test)

    def pp7(self):
        global test
        test += "g"
        x = random.randint(0, 9)
        self.p7.setText(str(x))
        #self.p7.setStyleSheet("background-color: red")
        self.label.setText(test)

    def pp8(self):
        global test
        test += "h"
        x = random.randint(0, 9)
        self.p8.setText(str(x))
        self.label.setText(test)

    def pp9(self):
        global test
        test += "i"
        x = random.randint(0, 9)
        self.p9.setText(str(x))
        self.label.setText(test)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()