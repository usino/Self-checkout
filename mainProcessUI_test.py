# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainProcessUI.ui'
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
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frameMain = QtWidgets.QFrame(self.centralwidget)
        self.frameMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMain.setObjectName("frameMain")
        self.gridLayout.addWidget(self.frameMain, 0, 1, 1, 1)
        self.frameMenu = QtWidgets.QFrame(self.centralwidget)
        self.frameMenu.setSizeIncrement(QtCore.QSize(0, 0))
        self.frameMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMenu.setObjectName("frameMenu")
        self.pushButton = QtWidgets.QPushButton(self.frameMenu)
        self.pushButton.setGeometry(QtCore.QRect(80, 120, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frameMenu)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 180, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frameMenu)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 250, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.frameMenu, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
