import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 450)
        self.setWindowTitle("My First Window")
        self.UI()

    def UI(self):
        self.text = QLabel("백억부자 이지운 PYQT5 정복중", self)
        
        self.name = QLineEdit(self)
        self.check = QCheckBox("체크박스", self)

        b1 = QPushButton("Enter", self)
        b2 = QPushButton("Exit", self)
        
        self.text.move(160, 50)
        self.name.move(120, 120)
        self.check.move(100, 150)

        b1.move(100, 80)
        b2.move(200, 80)

        b1.clicked.connect(self.b1_func)
        b2.clicked.connect(self.b2_func)

        self.show()

    def b1_func(self):
        self.text.setText("Enter가 눌림")
        self.text.resize(150 ,20)
        # print(self.name.text() + " 반가워용")
        QMessageBox.information(self, "정보정보", self.name.text()+ " 반가워용")

    def b2_func(self):
        self.text.setText("Exit가 눌림")
        self.text.resize(150 ,20)
        sys.exit()

App = QApplication(sys.argv)
window = MyWindow()
App.exec_()

