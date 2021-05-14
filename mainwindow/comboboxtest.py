import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, Qt


class ComboBoxTest(QWidget):
    def __init__(self):
        super(ComboBoxTest, self).__init__()
        self.initUi()

    def initUi(self):
        self.lbl = QLabel('Option1', self)
        self.lbl.move(50, 150)

        cB = QComboBox(self)
        cB.addItem('Option1')
        cB.addItem('Option2')
        cB.addItem('Option3')
        cB.addItem('Option4')
        cB.move(50, 50)

        cB.activated[str].connect(self.onActivated)

        self.setWindowTitle('QComboBox')
        self.setGeometry(600, 600, 600, 400)
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    comboTest = ComboBoxTest()
    app.exec_()
