# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\hokelin\pyCode\UI\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication,QWidget

class Ui_MainWindow(QMainWindow):
    lcdstring = '' #用来显示lcd上用来显示的字符
    operation = '' #定义一个操作符
    currNum = '' #当前值
    preNum = '' #上一个结果
    result = 0 #存放结果
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(70, 30, 681, 111))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setObjectName("lcdNumber")
        self.btnEqual = QtWidgets.QPushButton(self.centralwidget)
        self.btnEqual.setGeometry(QtCore.QRect(230, 430, 321, 40))
        self.btnEqual.setObjectName("btnEqual")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 160, 576, 248))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn1 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.horizontalLayout.addWidget(self.btn1)
        self.btn2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.horizontalLayout.addWidget(self.btn2)
        self.btn3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.horizontalLayout.addWidget(self.btn3)
        self.btnAdd = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn4 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.horizontalLayout_2.addWidget(self.btn4)
        self.btn5 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.horizontalLayout_2.addWidget(self.btn5)
        self.btn6 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.horizontalLayout_2.addWidget(self.btn6)
        self.btnPlus = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnPlus.setFont(font)
        self.btnPlus.setObjectName("btnPlus")
        self.horizontalLayout_2.addWidget(self.btnPlus)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn7 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.horizontalLayout_3.addWidget(self.btn7)
        self.btn8 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.horizontalLayout_3.addWidget(self.btn8)
        self.btn9 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.horizontalLayout_3.addWidget(self.btn9)
        self.btnChen = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnChen.setFont(font)
        self.btnChen.setObjectName("btnChen")
        self.horizontalLayout_3.addWidget(self.btnChen)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn0 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.horizontalLayout_4.addWidget(self.btn0)
        self.btnDot = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnDot.setFont(font)
        self.btnDot.setObjectName("btnDot")
        self.horizontalLayout_4.addWidget(self.btnDot)
        self.btnC = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnC.setFont(font)
        self.btnC.setObjectName("btnC")
        self.horizontalLayout_4.addWidget(self.btnC)
        self.btnDiv = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnDiv.setFont(font)
        self.btnDiv.setObjectName("btnDiv")
        self.horizontalLayout_4.addWidget(self.btnDiv)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(0, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 34))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)

        self.action()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def action(self):
        self.btn0.clicked.connect(self.numClicked)
        self.btn1.clicked.connect(self.numClicked)
        self.btn2.clicked.connect(self.numClicked)
        self.btn3.clicked.connect(self.numClicked)
        self.btn4.clicked.connect(self.numClicked)
        self.btn5.clicked.connect(self.numClicked)
        self.btn6.clicked.connect(self.numClicked)
        self.btn7.clicked.connect(self.numClicked)
        self.btn8.clicked.connect(self.numClicked)
        self.btn9.clicked.connect(self.numClicked)
        self.btnDot.clicked.connect(self.numClicked)

        self.btnAdd.clicked.connect(self.opClick)
        self.btnPlus.clicked.connect(self.opClick)
        self.btnChen.clicked.connect(self.opClick)
        self.btnDiv.clicked.connect(self.opClick)

        self.btnC.clicked.connect(self.clearClick)

        self.btnEqual.clicked.connect(self.equalClick)
    
    def numClicked(self): #输入数字和小数点
        if len(self.lcdstring) <= 27:
            s = self.sender()
            self.lcdstring = self.lcdstring + s.text()
            if str(self.lcdstring) == '.':
                self.lcdstring = '0.'
                self.lcdNumber.display(self.lcdstring)
                self.currNum = float(self.lcdstring)
            else:
                if str(self.lcdstring).count('.') > 1:
                    self.lcdstring = str(self.lcdstring)[:-1]
                    self.lcdNumber.display(self.lcdstring)
                    self.currNum = float(self.lcdstring)
                else:
                    self.lcdNumber.display(self.lcdstring)
                    self.currNum = float(self.lcdstring)
        else:
            pass

    def opClick(self):
        if self.operation != '':
            self.equalClick()
            self.preNum = self.currNum
            self.currNum = 0
            self.lcdstring = ''
            self.operation = self.sender().text()
        else:
            self.preNum = self.currNum
            self.currNum = 0
            self.lcdstring = ''
            self.operation = self.sender().text()

    def clearClick(self):
        self.lcdstring = ''
        self.operation = ''
        self.currNum = 0
        self.preNum = 0
        self.result = 0
        self.lcdNumber.display(0)
    def equalClick(self):
        if self.operation == '+':
            self.result = self.preNum + self.currNum
            self.lcdNumber.display(self.result)
        if self.operation == '-':
            self.result = self.preNum - self.currNum
            self.lcdNumber.display(self.result)
        if self.operation == '*':
            self.result = self.preNum * self.currNum
            self.lcdNumber.display(self.result)
        if self.operation == '/':
            if self.currNum == 0:
                self.lcdNumber.display('Error')
                self.result = 0
                self.preNum = 0
            else:
                self.result = self.preNum / self.currNum
                self.lcdNumber.display(self.result)
        self.currNum = self.result
        self.lcdstring = ''
        self.operation = ''

    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "示例"))
        self.btnEqual.setText(_translate("MainWindow", "="))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btnAdd.setText(_translate("MainWindow", "+"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btnPlus.setText(_translate("MainWindow", "-"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btnChen.setText(_translate("MainWindow", "*"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btnDot.setText(_translate("MainWindow", "."))
        self.btnC.setText(_translate("MainWindow", "C"))
        self.btnDiv.setText(_translate("MainWindow", "/"))

