import sys
import os

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog

from body import *
from word2img import img2text as i2t

name = ""
class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi("takeImage.ui", self)  # Load the .ui file

        self.pushButton.clicked.connect(self.URL_Editor)
        self.pushButton_2.clicked.connect(self.print_text)
        self.show()

    def URL_Editor(self):  # refine the photo URL

        global name
        name = name.replace(name, '')
        filename = QFileDialog.getOpenFileName()
        path = filename[0]

        for i in range(len(path) - 1, 0, -1):
            if path[i] == '/':
                break
            else:
                name += path[i]

        name = name[::-1]
        #print("Photo Name: "+name)

    def print_text(self):  # read text from photo

        text = i2t(name)
        in_file = 'Stat Attendance.txt'
        take_attendance(text, in_file)
        fi = open(in_file, 'r')  # read final data
        result = fi.read()

        self.textEdit.setText(result)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()

