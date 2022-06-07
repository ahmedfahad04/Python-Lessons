
################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import os
import platform
import sys

from PySide2 import QtCore, QtGui, QtWidgets
# IMPORT FUNCTIONS
from ui_function import *
# GUI FILE

from ui_toogle import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.tog = Ui_MainWindow()
        self.tog.setupUi(self)

        # toogle button activity
        self.tog.btn_toogle.clicked.connect(lambda: UI_function.toogle(self, 250))
        #self.tog.start_btn.clicked.connect(self.mytimer)



        #connecting pages
        self.tog.btn_1.clicked.connect(lambda: self.tog.stackedWidget.setCurrentWidget(self.tog.page_1))
        self.tog.btn_2.clicked.connect(lambda: self.tog.stackedWidget.setCurrentWidget(self.tog.page_2))
        self.tog.btn_3.clicked.connect(lambda: self.tog.stackedWidget.setCurrentWidget(self.tog.page_3))

        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
