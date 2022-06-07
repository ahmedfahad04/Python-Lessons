# -*- coding: utf-8 -*-
# rpcontacts/main.py

"""This module provides RP Contacts application."""

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)

from PySide2.QtWidgets import *
from views import Window


# class MainWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self, parent=None)
#         self.ui = Window()
#         self.ui.setupUi()
#

def main():
    """RP Contacts main function."""

    # Create the application
    app = QApplication()

    # Create the main window
    win = Window()
    win.show()

    # Run the event loop
    sys.exit(app.exec_())

main()