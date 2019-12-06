# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainProcessUI_5.ui'
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
        self.lable = QtWidgets.QLabel(self.centralwidget)
        self.lable.setObjectName("lable")
        self.gridLayout.addWidget(self.lable, 0, 0, 1, 1)
        self.btn_goback = QtWidgets.QPushButton(self.centralwidget)
        self.btn_goback.setObjectName("btn_goback")
        self.gridLayout.addWidget(self.btn_goback, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_goback.clicked.connect(self.btnGobackClick)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def btnGobackClick(self):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-family:\'微軟正黑體\'; font-size:18pt; color:#000000;\">完成扣款</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-family:\'微軟正黑體\'; font-size:18pt; color:#000000;\">結帳完成</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-family:\'微軟正黑體\'; font-size:18pt; color:#000000;\">10秒自動轉跳回首頁 ……</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.btn_goback.setText(_translate("MainWindow", "回首頁"))
