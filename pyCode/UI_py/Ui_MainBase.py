#所有主界面的基类，主要实现了退出的确认
from PyQt5 import QtCore, QtGui, QtWidgets
class MainBase(QtWidgets.QMainWindow):
    #是否可退出
    CanExit = True
    def closeEvent(self,event):
        if self.CanExit == True:
            reply = QtWidgets.QMessageBox.question(self,'警告','确认退出？',
                QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                event.accept()
                return
        event.ignore()
