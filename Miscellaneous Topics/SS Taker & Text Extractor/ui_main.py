# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainJXIsYq.ui'
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
        MainWindow.resize(753, 523)
        MainWindow.setMinimumSize(QSize(753, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Output = QFrame(self.centralwidget)
        self.Output.setObjectName(u"Output")
        self.Output.setMinimumSize(QSize(730, 450))
        self.Output.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Output.setFrameShape(QFrame.StyledPanel)
        self.Output.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Output)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.textEdit = QTextEdit(self.Output)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(730, 450))
        font = QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.textEdit)


        self.verticalLayout.addWidget(self.Output)

        self.Buttons = QFrame(self.centralwidget)
        self.Buttons.setObjectName(u"Buttons")
        self.Buttons.setMinimumSize(QSize(730, 50))
        self.Buttons.setFrameShape(QFrame.StyledPanel)
        self.Buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Buttons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sstaker = QPushButton(self.Buttons)
        self.sstaker.setObjectName(u"sstaker")
        self.sstaker.setMinimumSize(QSize(250, 30))
        self.sstaker.setFocusPolicy(Qt.NoFocus)
        self.sstaker.setToolTipDuration(-2)
        self.sstaker.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(170, 85, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u"Photos/camera.png", QSize(), QIcon.Normal, QIcon.On)
        self.sstaker.setIcon(icon)
        self.sstaker.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.sstaker)

        self.clear = QPushButton(self.Buttons)
        self.clear.setObjectName(u"clear")
        self.clear.setMinimumSize(QSize(250, 30))
        self.clear.setToolTipDuration(-2)
        self.clear.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(170, 85, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Photos/bin.jpg", QSize(), QIcon.Active, QIcon.On)
        self.clear.setIcon(icon1)
        self.clear.setIconSize(QSize(20, 20))
        self.clear.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.clear)


        self.verticalLayout.addWidget(self.Buttons, 0, Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.clear.clicked.connect(self.textEdit.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.textEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#0000ff;\">Canvas</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sstaker.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#0000ff;\">Take Screen Shot</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sstaker.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">SS</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sstaker.setText(QCoreApplication.translate("MainWindow", u"Take Screen Shot and Extract Text", None))
#if QT_CONFIG(tooltip)
        self.clear.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#0000ff;\">Clear Canvas</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.clear.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Clear</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.clear.setText(QCoreApplication.translate("MainWindow", u"Clear ", None))
    # retranslateUi

