import sys
from PyQt5.QtWidgets import *

import upbithts.main.maintab as appmaintab
import upbithts.investmentdetail.maintab as investmentmaintab
import upbithts.depositwithdrawal.maintab as depositmaintab
import upbithts.myaccount.maintab as myaccountmaintab


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.centerToWindow()
        self.initMain()
        self.setWindowTitle('Upbit HTS')

    def initMain(self):
        self.mainTab = appmaintab.MainTab()
        self.investmentDetail = investmentmaintab.MainTab()
        self.depositWithdrawal = depositmaintab.MainTab()
        self.myAccount = myaccountmaintab.MainTab()

        self.tabs = QTabWidget()
        self.tabs.addTab(self.mainTab, '메인')
        self.tabs.addTab(self.investmentDetail, '투자내역')
        self.tabs.addTab(self.depositWithdrawal, '입출금')
        self.tabs.addTab(self.myAccount, '내 정보')

        self.verticalBox = QVBoxLayout()
        self.verticalBox.addWidget(self.tabs)
        self.setLayout(self.verticalBox)

    def centerToWindow(self):
        qW = self.frameGeometry()
        qP = QDesktopWidget().availableGeometry().center()
        qW.moveCenter(qP)
        self.move(qW.topLeft())
        self.resize(800, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
