
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
import mainUI
import mainProcessUI
import mainProcessUI_1,mainProcessUI_2,mainProcessUI_3,mainProcessUI_4,mainProcessUI_5
import facerec_from_webcam 

name = None
count = None
myWinProcess = None
PushButton_1 = None
PushButton_2 = None
PushButton_3 = None
PushButton_4 = None
PushButton_5 = None


def btnClick_start(self, parameter_list=None):
    myWin.hide()
    global myWinProcess
    myWinProcess = MainProcessUI() #設定程序頁面
    myWinProcess.show()            #顯示程序頁面
    child = MainProcessUI_1()
    myWinProcess.gridLayout_4.addWidget(child)
    count = 1
    btnEnableOrNot(count)

def btnClick1_next(self, parameter_list=None):
    child = MainProcessUI_2()
    clearLayout(myWinProcess.gridLayout_4)
    myWinProcess.gridLayout_4.addWidget(child)
    count = 2
    btnEnableOrNot(count)
    
def btnClick2_next(self, parameter_list=None):
    child = MainProcessUI_3()
    clearLayout(myWinProcess.gridLayout_4)
    myWinProcess.gridLayout_4.addWidget(child)
    count = 3
    btnEnableOrNot(count)

def btnClick3_next(self, parameter_list=None):
    child = MainProcessUI_4()
    clearLayout(myWinProcess.gridLayout_4)
    myWinProcess.gridLayout_4.addWidget(child)
    count = 4
    btnEnableOrNot(count)

def btnClick4_next(self, parameter_list=None):
    child = MainProcessUI_5()
    clearLayout(myWinProcess.gridLayout_4)
    myWinProcess.gridLayout_4.addWidget(child)
    count = 5
    btnEnableOrNot(count)

def btnClick_goback(self, parameter_list=None):
    myWinProcess.hide()
    myWin.show()
    count = 0
    btnEnableOrNot(count)
    
def clearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()

def btnEnableOrNot(Count):
    if(Count==1):
        PushButton_1.setEnabled(True)
        PushButton_2.setEnabled(False)
        PushButton_3.setEnabled(False)
        PushButton_4.setEnabled(False)
        PushButton_5.setEnabled(False)
    elif(Count==2):
        PushButton_1.setEnabled(False)
        PushButton_2.setEnabled(True)
        PushButton_3.setEnabled(False)
        PushButton_4.setEnabled(False)
        PushButton_5.setEnabled(False)
    elif(Count==3):
        PushButton_1.setEnabled(False)
        PushButton_2.setEnabled(False)
        PushButton_3.setEnabled(True)
        PushButton_4.setEnabled(False)
        PushButton_5.setEnabled(False)
    elif(Count==4):
        PushButton_1.setEnabled(False)
        PushButton_2.setEnabled(False)
        PushButton_3.setEnabled(False)
        PushButton_4.setEnabled(True)
        PushButton_5.setEnabled(False)
    elif(Count==5):
        PushButton_1.setEnabled(False)
        PushButton_2.setEnabled(False)
        PushButton_3.setEnabled(False)
        PushButton_4.setEnabled(False)
        PushButton_5.setEnabled(True)
    else:
        pass    


#首頁
class MainUI(QMainWindow, mainUI.Ui_MainWindow, mainProcessUI.Ui_MainWindow, mainProcessUI_1.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.setupUi(self)
        self.btn_start.clicked.connect(btnClick_start)
     

#程序頁
class MainProcessUI(QMainWindow, mainProcessUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainProcessUI, self).__init__(parent)
        self.setupUi(self)

        global count #用來判斷左側按鈕是否開關
        count = 0

        global PushButton_1
        global PushButton_2
        global PushButton_3
        global PushButton_4
        global PushButton_5
        PushButton_1 = self.pushButton_1
        PushButton_2 = self.pushButton_2
        PushButton_3 = self.pushButton_3
        PushButton_4 = self.pushButton_4
        PushButton_5 = self.pushButton_5
        

#子程序頁1
class MainProcessUI_1(QMainWindow, mainProcessUI_1.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainProcessUI_1, self).__init__(parent)
        Facerec_from_webcam()
        self.setupUi(self)
        self.btn_next1.clicked.connect(btnClick1_next)
        print("nameINmainPUI_1:"+name)
        self.lab_who.setText(name)
        #顯示辨識結果圖
        pixmap = QPixmap('NEWpic.png')
        self.lab_img.setPixmap(pixmap)
        
        
#子程序頁2
class MainProcessUI_2(QMainWindow, mainProcessUI_2.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainProcessUI_2, self).__init__(parent)
        self.setupUi(self)
        self.btn_next2.clicked.connect(btnClick2_next)
        
        
#子程序頁3        
class MainProcessUI_3(QMainWindow, mainProcessUI_3.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainProcessUI_3, self).__init__(parent)
        self.setupUi(self)
        self.btn_next3.clicked.connect(btnClick3_next)

#子程序頁4        
class MainProcessUI_4(QMainWindow, mainProcessUI_4.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainProcessUI_4, self).__init__(parent)
        self.setupUi(self)
        self.btn_next4.clicked.connect(btnClick4_next)

#子程序頁5        
class MainProcessUI_5(QMainWindow, mainProcessUI_5.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainProcessUI_5, self).__init__(parent)
        self.setupUi(self)
        self.btn_goback.clicked.connect(btnClick_goback)


#人臉辨識
class Facerec_from_webcam(facerec_from_webcam.facerec_from_webcam):
    def __init__(self):
        super(Facerec_from_webcam, self).__init__()
        self.faceRecognition()
        global name
        name = self.nameback()
        print("getbackName:"+name)
        

#程式起點
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainUI()             #設定初始頁面為MainUI()
    myWin.show()                 #顯示初始頁面為MainUI()
    sys.exit(app.exec_())
