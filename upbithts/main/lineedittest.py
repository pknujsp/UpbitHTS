import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication


class LineEditTest(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        qLe = QLineEdit(self)
        qLe.move(60, 70)
        qLe.textChanged[str].connect(self.onChanged)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(400, 400, 400, 400)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LineEditTest()
    app.exec_()
