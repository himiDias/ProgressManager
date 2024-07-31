from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("University Progress Tracker")
        self.setGeometry(100,100,1000,800)

        menu_bar = self.menuBar()

        view_menu = menu_bar.addMenu('&View')
        help_menu = menu_bar.addMenu('&Help')

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
