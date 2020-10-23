import cv2
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from UI_py.Ui_untitled import Ui_MainWindow
from UI_py.Ui_MainBase import MainBase

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainBase()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
