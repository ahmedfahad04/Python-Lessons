import sys
import os

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog

from body import *
from word2img import img2text as i2t


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi("takeImage.ui", self)  # Load the .ui file

        self.pushButton.clicked.connect(self.URL_Editor)
        self.show()

    def URL_Editor(self):  # refine the photo URL
        filename = QFileDialog.getOpenFileName()
        path = filename[0]

        name = ""
        for i in range(len(path) - 1, 0, -1):
            if path[i] == '/':
                break
            else:
                name += path[i]

        name = name[::-1]


        self.pushButton_2.clicked.connect(lambda: self.print_text(name))  # note: lambda is used to take parameterized function

    def print_text(self, name):  # read text from photo
        print("Or here")
        text = i2t(name)

        print(text)
        take_attendance(text,"Stat Attendance.txt")

        fi = open('Final_Attendance.txt', 'r')  # read final data
        result = fi.read()
        print("Can you hear??")

        #self.textEdit.setText(result)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
