from PyQt5.QtWidgets import *

class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.setFixedHeight(500)
        self.setFixedWidth(300)



        print("Hello world")

        self.show()

app = QApplication([])

mw = main()
app.exec_()