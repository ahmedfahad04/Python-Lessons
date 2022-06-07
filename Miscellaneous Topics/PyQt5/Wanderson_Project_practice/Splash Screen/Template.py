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
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

## ==> import


## ==> GLOBALS


# YOUR APPLICATION
class SplashScreen(QMainWindow): #Replace 'SplashScreen' with any name you feel comfortable
    def __init__(self):
        QMainWindow.__init__(self)
        # self.ui = Ui_SplashScreen()   # Replace 'Ui_SplashScreen' with your class name in ui file
        self.ui.setupUi(self)
        ## UI ==> INTERFACE CODES
        ########################################################################

        


        ## SHOW ==> MAIN WINDOW
        ########################################################################

        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################

if __name__ == "__main__":
    app = QApplication()
    window = SplashScreen() # give name of your application class name
    sys.exit(app.exec_())
