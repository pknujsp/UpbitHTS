import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, Qt


class MainTab(QWidget):
    def __init__(self):
        super().__init__()
        qLabel = QLabel('myAccountTab', self)
        qLabel.move(100, 100)
