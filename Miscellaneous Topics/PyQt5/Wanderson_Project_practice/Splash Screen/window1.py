# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window1sIFhRs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 400)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 461, 361))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(195, 55, 100, 255), stop:1 rgba(29, 38, 113, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 50, 241, 101))
        font = QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"background-color:rgb(0, 255, 255);")
        self.pushButton.setAutoDefault(True)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 210, 241, 101))
        font1 = QFont()
        font1.setPointSize(15)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.pushButton_2.setAutoDefault(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u09aa\u09cd\u09b0\u09bf\u0995\u09be\u09b2\u099a\u09be\u09b0 \u09b6\u09c1\u09b0 \u0995\u09b0\u09c1\u09a8 </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u09aa\u09cd\u09b0\u09bf\u0995\u09be\u09b2\u099a\u09be\u09b0 \u09b6\u09c1\u09b0\u09c1 \u0995\u09b0\u09c1\u09a8 ", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u09aa\u09cd\u09b0\u09bf\u0995\u09be\u09b2\u099a\u09be\u09b0 \u09b6\u09c1\u09b0 \u0995\u09b0\u09c1\u09a8 </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u099f\u09cd\u09af\u09be\u0982\u0995\u09c7\u09b0 \u0985\u09ac\u09b8\u09cd\u09a5\u09be \u09aa\u09b0\u09cd\u09af\u09ac\u09c7\u0995\u09cd\u09b7\u09a8 \u0995\u09b0\u09c1\u09a8 ", None))
    # retranslateUi

