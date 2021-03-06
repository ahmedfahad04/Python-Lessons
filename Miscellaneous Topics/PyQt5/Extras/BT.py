# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BUttonTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainBox = QtWidgets.QGroupBox(self.centralwidget)
        self.MainBox.setGeometry(QtCore.QRect(100, 40, 361, 301))
        self.MainBox.setStyleSheet("border-width: 5px")
        self.MainBox.setTitle("")
        self.MainBox.setObjectName("MainBox")
        self.pushButton = QtWidgets.QPushButton(self.MainBox)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 121, 101))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.MainBox)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 0, 121, 101))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.MainBox)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 0, 121, 101))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.MainBox)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 70, 121, 101))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.MainBox)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 70, 121, 101))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.MainBox)
        self.pushButton_7.setGeometry(QtCore.QRect(240, 100, 121, 101))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.MainBox)
        self.pushButton_8.setGeometry(QtCore.QRect(120, 100, 121, 101))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.MainBox)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 100, 121, 101))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.MainBox)
        self.pushButton_10.setGeometry(QtCore.QRect(240, 200, 121, 101))
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.MainBox)
        self.pushButton_11.setGeometry(QtCore.QRect(120, 200, 121, 101))
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.MainBox)
        self.pushButton_12.setGeometry(QtCore.QRect(0, 200, 121, 101))
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 360, 361, 41))
        self.textEdit.setObjectName("textEdit")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.printmsg)
        self.pushButton_2.clicked.connect(self.printmsg2)
        self.pushButton_11.clicked.connect(self.printmsg11)
        self.pushButton_12.clicked.connect(self.printmsg12)
        self.pushButton_5.clicked.connect(self.printmsg5)
        self.pushButton_7.clicked.connect(self.printmsg7)
        self.pushButton_8.clicked.connect(self.printmsg8)
        self.pushButton_9.clicked.connect(self.printmsg9)
        self.pushButton_10.clicked.connect(self.printmsg10)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def printmsg(self):
        x = random.randint(0,9)
        self.pushButton.setText(str(x))
        self.textEdit.setText("1")

    def printmsg2(self):
        x = random.randint(0,9)
        self.pushButton_2.setText(str(x))
        self.textEdit.setText("2")

    def printmsg11(self):
        x = random.randint(0,9)
        self.pushButton_11.setText(str(x))
        self.textEdit.setText("11")

    def printmsg12(self):
        x = random.randint(0,9)
        self.pushButton_12.setText(str(x))
        self.textEdit.setText("12")

    def printmsg5(self):
        x = random.randint(0,9)
        self.pushButton_5.setText(str(x))
        self.textEdit.setText("5")

    def printmsg7(self):
        x = random.randint(0, 9)
        self.pushButton_7.setText(str(x))
        self.textEdit.setText("7")

    def printmsg8(self):
        x = random.randint(0, 9)
        self.pushButton_8.setText(str(x))
        self.textEdit.setText("8")

    def printmsg9(self):
        x = random.randint(0, 9)
        self.pushButton_9.setText(str(x))
        self.textEdit.setText("9")

    def printmsg10(self):
        x = random.randint(0, 9)
        self.pushButton_10.setText(str(x))
        self.textEdit.setText("10")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
