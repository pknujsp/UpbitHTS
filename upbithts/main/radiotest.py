import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class RadioTest(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        rbtn1 = QRadioButton('First Btn', self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)

        rbtn2 = QRadioButton('Second Btn', self)
        rbtn2.move(rbtn1.x(), rbtn1.y() + 20)
        rbtn2.setText('Second Btn')

        self.setGeometry(400, 400, 600, 400)
        self.setWindowTitle('QRadioBtn')
        self.show()

    def toggledBtn(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('CLICKED')
        else:
            self.setWindowTitle('NOT')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    radioTest = RadioTest()
    app.exec_()
