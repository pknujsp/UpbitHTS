import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, Qt, QDateTime
from PyQt5.QtGui import QFont


class PushBtn(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.center()

    def initUi(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)

        label1 = QLabel('btn1Label', self)
        label1.setAlignment(Qt.AlignHCenter)
        label2 = QLabel('btn2Label', self)
        label3 = QLabel('btn3Label', self)

        gridLayout = QGridLayout()
        gridLayout.addWidget(label1, 0, 0)
        gridLayout.addWidget(label2, 1, 0)
        gridLayout.addWidget(label3, 2, 0)

        gridLayout.addWidget(btn1, 0, 1)
        gridLayout.addWidget(btn2, 1, 1)
        gridLayout.addWidget(btn3, 2, 1)

        self.setLayout(gridLayout)
        self.setWindowTitle('QPushButton')
        self.resize(600, 500)
        self.show()

    def center(self):
        qW = self.frameGeometry()
        qP = QDesktopWidget().availableGeometry().center()
        qW.moveCenter(qP)
        self.move(qW.topLeft())


app = QApplication(sys.argv)
pushBtn = PushBtn()
app.exec_()
