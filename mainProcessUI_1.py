# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainProcessUI_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
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
        self.btn_next1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next1.setObjectName("btn_next1")
        self.gridLayout.addWidget(self.btn_next1, 1, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lab_recognizePeopleOrNot = QtWidgets.QLabel(self.centralwidget)
        self.lab_recognizePeopleOrNot.setObjectName("lab_recognizePeopleOrNot")
        self.verticalLayout.addWidget(self.lab_recognizePeopleOrNot)
        self.lab_who = QtWidgets.QLabel(self.centralwidget)
        self.lab_who.setObjectName("lab_who")
        self.verticalLayout.addWidget(self.lab_who)
        self.gridLayout.addLayout(self.verticalLayout, 0, 3, 1, 1)
        self.lab_img = QtWidgets.QLabel(self.centralwidget)
        self.lab_img.setObjectName("lab_img")
        self.gridLayout.addWidget(self.lab_img, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.btn_next1.clicked.connect(self.XX)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def XX(self):
        pass


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_next1.setText(_translate("MainWindow", "下一步"))
        self.lab_recognizePeopleOrNot.setText(_translate("MainWindow", "( 辨識會員中 )"))
        self.lab_who.setText(_translate("MainWindow", "XXX"))
        self.lab_img.setText(_translate("MainWindow", "TextLabel"))

