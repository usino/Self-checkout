# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainProcessUI_2.ui'
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btn_next2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next2.setObjectName("btn_next2")
        self.gridLayout.addWidget(self.btn_next2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_next2.clicked.connect(self.btnNext2Click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def btnNext2Click(self):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-family:\'微軟正黑體\'; font-size:32pt; color:#000000;\">放置商品</span></p><p align=\"center\"><span style=\" font-family:\'微軟正黑體\'; font-size:18pt; color:#000000;\">請放置商品，完成後請點擊下一步</span><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.btn_next2.setText(_translate("MainWindow", "下一步"))
