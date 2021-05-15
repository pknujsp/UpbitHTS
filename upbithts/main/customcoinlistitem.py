import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CustomCoinListItemWidget(QWidget):
    def __init__(self, coinName, marketCode, parent=None):
        super(CustomCoinListItemWidget, self).__init__(parent)

        self.__coinName = coinName
        self.__marketCode = marketCode

        self.rootQHBoxLayout = QHBoxLayout()
        self.coinNameVBoxLayout = QVBoxLayout()
        self.coinChangeVBoxLayout = QVBoxLayout()

        self.coinNameLabel = QLabel()
        self.coinMarketCodeLabel = QLabel()
        self.coinCurrentPriceLabel = QLabel()
        self.coinChangeRateLabel = QLabel()
        self.coinChangePriceLabel = QLabel()
        self.coinTradePriceLabel = QLabel()
        self.coinTradeVolumeLabel = QLabel()

        self.coinNameLabel.setText(self.__coinName)
        self.coinMarketCodeLabel.setText(self.__marketCode)

        self.coinNameVBoxLayout.addWidget(self.coinNameLabel, 2)
        self.coinNameVBoxLayout.addWidget(self.coinMarketCodeLabel, 1)

        self.coinChangeVBoxLayout.addWidget(self.coinChangeRateLabel, 2)
        self.coinChangeVBoxLayout.addWidget(self.coinChangePriceLabel, 1)

        self.rootQHBoxLayout.addLayout(self.coinNameVBoxLayout, 2)
        self.rootQHBoxLayout.addWidget(self.coinCurrentPriceLabel, 1)
        self.rootQHBoxLayout.addLayout(self.coinChangeVBoxLayout, 1)
        self.rootQHBoxLayout.addWidget(self.coinTradePriceLabel, 1)

        self.setLayout(self.rootQHBoxLayout)

    def setData(self, currentPrice, changeRate, changePrice, tradePrice):
        self.coinCurrentPriceLabel.setText(str(currentPrice))
        self.coinChangeRateLabel.setText(str(changeRate))
        self.coinChangePriceLabel.setText(str(changePrice))
        self.coinTradePriceLabel.setText(str(tradePrice))

        self.changeTextColor(changeRate)

    def changeTextColor(self, changeRate):
        changeRateFloat = float(changeRate)
        color = '''color: rgb(255, 0, 0);''' if changeRateFloat < 0.0 else '''color: rgb(0, 0, 255);'''

        self.coinCurrentPriceLabel.setStyleSheet(color)
        self.coinChangeRateLabel.setStyleSheet(color)
        self.coinChangePriceLabel.setStyleSheet(color)

    @property
    def coinName(self):
        return self.__coinName

    @property
    def marketCode(self):
        return self.__marketCode
