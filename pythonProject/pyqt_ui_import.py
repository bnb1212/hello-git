import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:\study\pythonProject\pyqt_ui.ui")[0]

#화면을 띄우는데 사용되는 Class 선언    
class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.b1.clicked.connect(self.b1_func)
        self.b2.clicked.connect(self.b2_func)

    def b2_func(self):
        mbox = QMessageBox.question(self, "Warning", "Really do you want exit?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()

    def b1_func(self):
        QMessageBox.information(self, 'infomation', '반가워요')


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()