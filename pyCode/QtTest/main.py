# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from dialog import *
class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec_())
