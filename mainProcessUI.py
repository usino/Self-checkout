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
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frameMenu = QtWidgets.QFrame(self.centralwidget)
        self.frameMenu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frameMenu.setSizeIncrement(QtCore.QSize(0, 0))
        self.frameMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMenu.setObjectName("frameMenu")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frameMenu)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frameMenu)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frameMenu)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frameMenu)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 5, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frameMenu)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.frameMenu)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_3.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frameMenu)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)
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
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
