######################################################
##
## BY: Fahad
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
#######################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)

from PySide2.QtWidgets import *
from ui_main import *
import pyautogui as pg
from word2img import img2text as i2t
import time
import cv2
import pytesseract

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.obj = Ui_MainWindow()
        self.obj.setupUi(self)

        self.obj.sstaker.clicked.connect(self.act)
        self.show()


    def act(self):
        self.setWindowState(Qt.WindowMinimized)
        time.sleep(0.5)
        ss = pg.screenshot()
        print("Screen Shot Done!!")
        ss.save(r"F:\FAHADS FILES\__PYTHON__\Home_Experiments\Python Home Helper\SS Taker & Text Extractor\shots.png")
        txt = i2t("F:\FAHADS FILES\__PYTHON__\Home_Experiments\Python Home Helper\SS Taker & Text Extractor\shots.png")

        cnt = 0
        for word in txt:
            if word == '\n':
                cnt += 1

        print("Lines: ", cnt)

        self.obj.textEdit.setText(txt)
        self.show()



#if __name__=="__main__":
app = QApplication()
window = MainWindow()
sys.exit(app.exec_())