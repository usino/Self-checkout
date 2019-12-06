import sys
import os
import cv2
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap

img_count = 1
global showImage

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        self.timer_camera = QtCore.QTimer()  # 初始化定時器
        self.cap = cv2.VideoCapture(0)  # 初始化攝像頭
        self.CAM_NUM = 0
        self.set_ui()
        self.slot_init()
        self.__flag_work = 0
        self.x = 0
        self.count = 0

    def set_ui(self):
        self.__layout_main = QtWidgets.QHBoxLayout()  # 採用QHBoxLayout類，按照從左到右的順序來添加控件
        self.__layout_fun_button = QtWidgets.QHBoxLayout()
        self.__layout_data_show = QtWidgets.QVBoxLayout()  # QVBoxLayout類垂直地擺放小部件
        
        #設定1個btn(打開相機)
        self.button_open_camera = QtWidgets.QPushButton(u'打開相機')
        self.button_open_camera.setMinimumHeight(50)

        #設定1個btn(退出)
        self.button_close = QtWidgets.QPushButton(u'退出')
        self.button_close.setMinimumHeight(50)

        #設定1個btn(退出)
        self.button_Screenshot = QtWidgets.QPushButton(u'截圖')
        self.button_Screenshot.setMinimumHeight(50)

        #裝入__layout_fun_button中
        self.__layout_fun_button.addWidget(self.button_open_camera)
        self.__layout_fun_button.addWidget(self.button_close)
        self.__layout_fun_button.addWidget(self.button_Screenshot)

        # 設定1個lab(放攝像機影像，顯示用)
        self.label_show_camera = QtWidgets.QLabel()
        self.label_show_camera.setFixedSize(641, 481)
        self.label_show_camera.setAutoFillBackground(False)

        #裝入__layout_main.addLayout中
        self.__layout_main.addLayout(self.__layout_fun_button)
        self.__layout_main.addWidget(self.label_show_camera)

        #設定 "主layout"
        self.setLayout(self.__layout_main)
        #設定視窗名稱
        self.setWindowTitle(u'攝像頭')
        # move()方法是移動窗口在屏幕上的位置到x = 500，y = 500的位置上
        self.move(500, 500)

    def slot_init(self):  # 設定對應事件(建立通信連接)
        self.button_open_camera.clicked.connect(self.button_open_camera_click)
        self.button_Screenshot.clicked.connect(self.button_Screenshot_click)
        self.timer_camera.timeout.connect(self.show_camera)
        self.button_close.clicked.connect(self.close)

    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.Warning(self, u'Warning', u'請檢測相機與電腦是否連接正確',
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
                if msg==QtGui.QMessageBox.Cancel:
                                    pass
            else:
                self.timer_camera.start(30)
                self.button_open_camera.setText(u'關閉相機')
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.label_show_camera.clear()
            self.button_open_camera.setText(u'打開相機')

    def show_camera(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def button_Screenshot_click(self):
        cv2.imwrite("./NEWpic.png",self.image)


    def closeEvent(self, event):
        ok = QtWidgets.QPushButton()
        cancel = QtWidgets.QPushButton()
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u'關閉', u'是否關閉！')
        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cancel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'確定')
        cancel.setText(u'取消')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            event.ignore()
        else:
            if self.cap.isOpened():
                self.cap.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            event.accept()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(App.exec_())