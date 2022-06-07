from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow 
from main import *
from time import *
from PyQt5 import *
import os

class UI_function(QMainWindow):
    def toogle(self, maxSize):

        width = self.tog.left_menu.width()
        maxWidth = maxSize
        standard = 80

        if width == 80:
            widthExtd = maxWidth
        else:
            widthExtd = standard

        self.animation = QtCore.QPropertyAnimation(self.tog.left_menu, b"minimumWidth")
        self.animation.setDuration(400)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtd)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    # def currentTime(self):
    #     while True:
    #         tt = localtime()
    #         curTime = strftime("%H:%M:%S", tt)
    #         self.tog.label.setText(curTime)
    #         print(curTime)
    #         sleep(1)
    def mytimer(self):
        clear = lambda: os.system('cls')
        min = 0
        k = 0
        while True:
            if k == 10:
                min += 1
            k = k%10
            print("Min: %d Sec: %d" % (min, k % 10))
            self.tog.label.setText("Min: {} Sec: {}".format(min,k))

            clear()
            sleep(1)
            k += 1