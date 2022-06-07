# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_loadingyGADSo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(624, 403)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_widget = QFrame(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setGeometry(QRect(10, 10, 601, 381))
        self.main_widget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 49, 148, 255), stop:0.75 rgba(0, 7, 20, 255));\n"
"border-radius: 10px")
        self.main_widget.setFrameShape(QFrame.StyledPanel)
        self.main_widget.setFrameShadow(QFrame.Raised)
        self.app_name = QLabel(self.main_widget)
        self.app_name.setObjectName(u"app_name")
        self.app_name.setGeometry(QRect(0, 70, 601, 61))
        font = QFont()
        font.setFamily(u"Segoe MDL2 Assets")
        font.setPointSize(40)
        self.app_name.setFont(font)
        self.app_name.setStyleSheet(u"background-color: none;")
        self.loading = QLabel(self.main_widget)
        self.loading.setObjectName(u"loading")
        self.loading.setGeometry(QRect(0, 310, 601, 31))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        self.loading.setFont(font1)
        self.loading.setStyleSheet(u"background-color: none;\n"
"")
        self.app_description = QLabel(self.main_widget)
        self.app_description.setObjectName(u"app_description")
        self.app_description.setGeometry(QRect(0, 130, 601, 41))
        font2 = QFont()
        font2.setPointSize(14)
        self.app_description.setFont(font2)
        self.app_description.setStyleSheet(u"background-color: none;\n"
"")
        self.progressBar = QProgressBar(self.main_widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 280, 531, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(1, 77, 255, 255), stop:1 rgba(255, 32, 32, 255));\n"
"\n"
"}")
        self.progressBar.setValue(23)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.close_btn = QPushButton(self.main_widget)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(570, 10, 21, 21))
        self.close_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;		\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.close_btn_2 = QPushButton(self.main_widget)
        self.close_btn_2.setObjectName(u"close_btn_2")
        self.close_btn_2.setGeometry(QRect(510, 10, 21, 21))
        self.close_btn_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;		\n"
"	background-color: rgb(85, 255, 0);\n"
"}\n"
"QPushButton:hover {		\n"
"	\n"
"	background-color: rgb(58, 173, 0);\n"
"}")
        self.close_btn_3 = QPushButton(self.main_widget)
        self.close_btn_3.setObjectName(u"close_btn_3")
        self.close_btn_3.setGeometry(QRect(540, 10, 21, 21))
        self.close_btn_3.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;		\n"
"	background-color: rgb(0, 191, 191);\n"
"}\n"
"QPushButton:hover {		\n"
"	\n"
"	background-color: rgb(0, 144, 144);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#bed848;\">Your</span><span style=\" color:#bed848;\"> APP NAME</span></p></body></html>", None))
        self.loading.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#7b849f;\">Loading...</span></p></body></html>", None))
        self.app_description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#6272a4;\">App Description</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.close_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">X</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.close_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.close_btn_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">X</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.close_btn_2.setText("")
#if QT_CONFIG(whatsthis)
        self.close_btn_3.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">X</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.close_btn_3.setText("")
    # retranslateUi

