################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


## ==> import
from ui_splash_screen import *

## ==> GLOBALS
counter = 0

class sub(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setuUi(self)

# YOUR APPLICATION
class MainWindow(QMainWindow):  # Replace 'SplashScreen' with any name you feel comfortable
    def __init__(self):
        QMainWindow.__init__(self)
        self.fahad = Ui_MainWindow()   # Replace 'Ui_SplashScreen' with your class name in ui file
        self.fahad.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        #Remove top Bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) #remove the top bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) #remove white blank bg

        #Progress Bar
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(50)

        #button action
        self.fahad.close_btn.clicked.connect(self.stop)
        self.fahad.close_btn_2.clicked.connect(self.min)
        self.fahad.close_btn_3.clicked.connect(self.max)

        #Show time
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.showTime)
        self.timer2.start() #1 second
        self.showTime()

        ## ==> END ##
        self.show()
    ## ==> APP FUNCTIONS
    ########################################################################

    #progress bar update
    def progress(self):
        global counter
        self.fahad.progressBar.setValue(counter) #setting progress bar value

        if counter > 100:
            self.timer.stop()
            self.close()

        counter += 1

    #close screen
    def stop(self):
        self.close()

    #minimize screen
    def min(self):
        self.setWindowState(Qt.WindowMinimized)

    #maximize screen
    def max(self):
        self.setWindowState(Qt.WindowMaximized)

    # Time Show
    def showTime(self):
        currentTime = QTime.currentTime()

        displayTxt = currentTime.toString('mm:ss')
        print(displayTxt)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()  # give name of your application class name
    sys.exit(app.exec_())
