from PyQt5.QtWidgets import *
from PyQt5 import uic


class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        uic.loadUi("tab.ui", self)

        self.show()


app = QApplication([])
mw = mainwindow()
app.exec_()
