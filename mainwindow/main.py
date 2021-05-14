import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, Qt, QDateTime
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.toolbar = self.addToolBar('Quit')
        self.initUi()

    def initUi(self):
        self.setWindowTitle('Upbit HTS')
        self.resize(600, 400)
        self.center()

        self.initTooltips()
        self.initStatusBar()
        self.initToolbar()
        self.initCurrentDateTime()
        self.addViews()

        btn = QPushButton('종료', self)
        btn.move(100, 100)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

    def addViews(self):
        label1, label2 = QLabel('Label1', self), QLabel('Label2', self)
        label1.move(20, 20)
        label2.move(20, 60)

        btn1, btn2 = QPushButton('Btn1', self), QPushButton('Btn2', self)
        btn1.move(label1.x() + label1.width(), label1.y())
        btn2.move(label2.x() + label2.width(), label2.y())

    def center(self):
        qWidget = self.frameGeometry()
        qPoint = QDesktopWidget().availableGeometry().center()
        qWidget.moveCenter(qPoint)
        self.move(qWidget.topLeft())

    def initTooltips(self):
        tooltipBtn = QPushButton('Tooltip', self)
        tooltipBtn.setToolTip('tooltip message')
        tooltipBtn.move(150, 150)
        tooltipBtn.resize(tooltipBtn.sizeHint())

    def initStatusBar(self):
        self.statusBar().showMessage('Ready')

    def initToolbar(self):
        quitAction = QAction('Quit', self)
        quitAction.setStatusTip('Quit Application')
        quitAction.triggered.connect(qApp.quit)
        self.toolbar.addAction(quitAction)

    def initCurrentDateTime(self):
        datetime = QDateTime.currentDateTime()
        self.statusBar().showMessage(datetime.currentDateTime().toString('yyyy/MM/dd hh:mm:ss'))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
