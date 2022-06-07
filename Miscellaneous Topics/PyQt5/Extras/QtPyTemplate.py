from PyQt5.QtWidgets import *
#from Home_Experiments.PyQt5.Extras.ui_tab import Ui_MainWindow
from ui_tab import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


        self.show()


app = QApplication([])
mw = MainWindow()
app.exec_()

