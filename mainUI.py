# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setObjectName("btn_start")
        self.gridLayout_2.addWidget(self.btn_start, 1, 0, 1, 1)
        self.lab_welcome = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lab_welcome.setFont(font)
        self.lab_welcome.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lab_welcome.setTextFormat(QtCore.Qt.AutoText)
        self.lab_welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_welcome.setWordWrap(False)
        self.lab_welcome.setObjectName("lab_welcome")
        self.gridLayout_2.addWidget(self.lab_welcome, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_start.clicked.connect(self.btnStartClick)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def btnStartClick(self):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_start.setText(_translate("MainWindow", "START"))
        self.lab_welcome.setText(_translate("MainWindow", "歡迎使用\n"
"第一科技無人結帳系統"))
