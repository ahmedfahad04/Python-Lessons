from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import *
import time

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        btn = QPushButton("Regster")
        tf = QLineEdit()
        tf.setPlaceholderText("Enter your Password: ")
        
        btn.clicked.connect(lambda: self.action(tf.text()))
        layout.addWidget(tf)
        layout.addWidget(btn)

        self.setLayout(layout)
        self.show()

    def msgBox(self, message, icon):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(message)
        msg.setWindowTitle("Confirm Password")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

    def action(self, txt):
        if txt=="1224":
            print("Correct Password")
            
            self.close()
            self.msgBox("Registration Successful", QMessageBox.Information)
        else:
            self.msgBox("You have entered Wrong password. Please try again later.", QMessageBox.Warning)

   


app = QApplication([])
mw = MainWindow()
app.exec_()