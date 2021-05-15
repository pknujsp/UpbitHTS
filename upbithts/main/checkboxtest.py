import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, Qt


class TestCheckBoxWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        cB = QCheckBox('Show title', self)
        cB.move(20, 20)
        cB.toggle()
        cB.stateChanged.connect(self.changeTitle)

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('Empty')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestCheckBoxWindow()
    app.exec_()
