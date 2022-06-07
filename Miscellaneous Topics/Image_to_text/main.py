# from word2img import img2text as i2t
# text = i2t('d2.png')
# print(text)
#
# import cv2
# print("GeeksForGeeks")
# print("Your OpenCV version is: " + cv2.__version__)

# print("TESSERACT:: ")
# import pytesseract as pt
# from PIL import Image
#
# pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# path = "d2.png"
# value = Image.open(path)
# text = pt.image_to_string(value)
# print(text)

from word2img import img2text as i2t
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from PIL import Image
import pytesseract as pt
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi("takeImage.ui", self) # Load the .ui file

        self.pushButton.clicked.connect(self.URL_Editor)

        self.show()
    def URL_Editor(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]

        name = ""
        for i in range(len(path) - 1, 0, -1):
            if path[i] == '/':
                break
            else:
                name += path[i]

        name = name[::-1]

        self.pushButton_2.clicked.connect(lambda: self.print_text(name)) #note: lambda is used to take parameterized function


    def print_text(self, name):
        text = i2t(name)
        # # print(text)
        # value = Image.open(str(name))
        # text = pt.image_to_string(value)
        out = open("participants.txt", 'a+')
        try:
            out.write(text.lower())
            print("Data Saved!!")
        except:
            pass
        self.textEdit.setText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()