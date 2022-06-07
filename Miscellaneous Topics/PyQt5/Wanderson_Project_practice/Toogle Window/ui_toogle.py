# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_toogleHMbYHx.ui'
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
        MainWindow.resize(700, 350)
        MainWindow.setMinimumSize(QSize(700, 350))
        MainWindow.setStyleSheet(u"background-color: rgba(55, 55, 55, 235);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TopBar = QFrame(self.centralwidget)
        self.TopBar.setObjectName(u"TopBar")
        self.TopBar.setMaximumSize(QSize(16777215, 40))
        self.TopBar.setSizeIncrement(QSize(0, 0))
        self.TopBar.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.TopBar.setFrameShape(QFrame.NoFrame)
        self.TopBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.TopBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toogle = QFrame(self.TopBar)
        self.toogle.setObjectName(u"toogle")
        self.toogle.setMaximumSize(QSize(80, 40))
        self.toogle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.toogle.setFrameShape(QFrame.StyledPanel)
        self.toogle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.toogle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_toogle = QPushButton(self.toogle)
        self.btn_toogle.setObjectName(u"btn_toogle")
        self.btn_toogle.setMinimumSize(QSize(70, 40))
        self.btn_toogle.setMaximumSize(QSize(80, 40))
        self.btn_toogle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px")

        self.verticalLayout_2.addWidget(self.btn_toogle)


        self.horizontalLayout.addWidget(self.toogle)

        self.top = QFrame(self.TopBar)
        self.top.setObjectName(u"top")
        self.top.setMaximumSize(QSize(16777215, 40))
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.top)


        self.verticalLayout.addWidget(self.TopBar)

        self.Container = QFrame(self.centralwidget)
        self.Container.setObjectName(u"Container")
        self.Container.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.Container.setFrameShape(QFrame.NoFrame)
        self.Container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.Container)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(80, 0))
        self.left_menu.setMaximumSize(QSize(16777215, 16777215))
        self.left_menu.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QFrame(self.left_menu)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setMaximumSize(QSize(16777215, 16777215))
        self.menu_btn.setFrameShape(QFrame.StyledPanel)
        self.menu_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.menu_btn)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_1 = QPushButton(self.menu_btn)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setMinimumSize(QSize(0, 40))
        self.btn_1.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(50, 50, 50);\n"
"	border: 0px solid\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_1)

        self.btn_2 = QPushButton(self.menu_btn)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setMinimumSize(QSize(0, 40))
        self.btn_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(50, 50, 50);\n"
"	border: 0px solid\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_2)

        self.btn_3 = QPushButton(self.menu_btn)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setMinimumSize(QSize(0, 40))
        self.btn_3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(50, 50, 50);\n"
"	border: 0px solid\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_3)


        self.verticalLayout_3.addWidget(self.menu_btn, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.left_menu)

        self.menu_pages_2 = QFrame(self.Container)
        self.menu_pages_2.setObjectName(u"menu_pages_2")
        self.menu_pages_2.setStyleSheet(u"")
        self.menu_pages_2.setFrameShape(QFrame.StyledPanel)
        self.menu_pages_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.menu_pages_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.menu_pages_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_6 = QVBoxLayout(self.page_1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 10, 391, 181))
        font = QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(60, 65, 70);\n"
"color: #fff")
        self.label.setAlignment(Qt.AlignCenter)
        self.start_btn = QPushButton(self.frame)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setGeometry(QRect(100, 230, 121, 51))
        self.start_btn.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 65, 70);\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(13, 96, 168);\n"
"}")
        self.stop_btn = QPushButton(self.frame)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setGeometry(QRect(360, 230, 121, 51))
        self.stop_btn.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 65, 70);\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(13, 96, 168);\n"
"}")

        self.verticalLayout_6.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 65, 70);")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 65, 70);")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.menu_pages_2)


        self.verticalLayout.addWidget(self.Container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toogle.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"Page 3", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current Time", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About Us", None))
    # retranslateUi

