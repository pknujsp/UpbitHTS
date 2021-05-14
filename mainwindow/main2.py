import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        okBtn = QPushButton('OK')
        cancelBtn = QPushButton('CANCEL')

        hBox = QHBoxLayout()
        hBox.addStretch(1)
        hBox.addWidget(okBtn)
        hBox.addWidget(cancelBtn)
        hBox.addStretch(1)
        vBox = QVBoxLayout()
        vBox.addStretch(3)
        vBox.addLayout(hBox)

        self.setLayout(vBox)
        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec_()
