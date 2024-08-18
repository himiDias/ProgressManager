from PyQt5.QtWidgets import QApplication 
from view import MainWindow
from controller import Controller

if __name__ == "__main__":
    app = QApplication([])

    # Initialize main window and view
    view = MainWindow()

    # Initialize controller with model and view
    controller = Controller(view)

    # Show the login view
    view.show()

    app.exec_()
