import json
import pyupbit
import requests
from PyQt5 import QtCore
from PyQt5.uic.properties import QtGui

import upbithts.main.tablecolumn.commonutil as commonutil

from PyQt5.QtWidgets import *


class MainTab(QWidget):
    def __init__(self):
        super().__init__()
        self.coinNameDict = dict()
        self.marketCodeDict = dict()

        self.searchCoinLineEdit = QLineEdit(self)
        self.searchCoinLineEdit.setPlaceholderText('코인명/심볼 검색')
        self.searchCoinBtn = QPushButton('검색', self)

        self.searchCoinBtn.clicked.connect(self.requestTicker)

        self.searchCoinBox = QHBoxLayout()
        self.searchCoinBox.addWidget(self.searchCoinLineEdit, 3)
        self.searchCoinBox.addWidget(self.searchCoinBtn, 1)

        self.coinTable = QTableWidget(self)
        self.coinTable.setSortingEnabled(False)
        self.coinTable.setColumnCount(4)
        self.coinTable.setHorizontalHeaderLabels(['코인명', '현재가', '전일대비', '거래대금'])

        self.coinInfoView = QFrame()
        self.coinInfoView.setFrameShape(QFrame.Box)

        self.coinViewsBox = QHBoxLayout()
        self.coinViewsBox.addWidget(self.coinTable, 3)
        self.coinViewsBox.addWidget(self.coinInfoView, 1)

        self.rootLayout = QVBoxLayout()
        self.rootLayout.addLayout(self.searchCoinBox)
        self.rootLayout.addLayout(self.coinViewsBox)

        self.setLayout(self.rootLayout)

        self.requestMarketCode()

    def showCurrentPrice(self):
        ticker = "KRW-ETH"
        currPrice = pyupbit.get_current_price(ticker)
        currPriceLabel = QLabel(self)
        currPriceLabel.setText(str(currPrice))

    def requestTicker(self):
        text = self.searchCoinLineEdit.text()
        self.addRow(text)
        coinInfo = self.getCoinInfo(text)
        coinName = coinInfo['coin_name']
        marketCode = coinInfo['market_code']

        url = "https://api.upbit.com/v1/ticker"
        querystring = {"markets": marketCode}
        headers = {"Accept": "application/json"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.text)
        self.resultTicker(result, coinName)

    def resultTicker(self, result, coinName):
        rowIndex = ''
        for row in range(0, self.coinTable.rowCount()):
            item = self.coinTable.item(row, 0)
            if coinName == item.text():
                rowIndex = row
                break

        resultDict = result[0]
        self.coinTable.item(rowIndex, 1).setText(str(resultDict['trade_price']))
        self.coinTable.item(rowIndex, 2).setText(
            str(resultDict['change_rate']) + '\n' + str(resultDict['change_price']))
        # commonutil.changeTextColor(self.coinTable.item(rowIndex, 1), resultDict['change_rate'])
        # commonutil.changeTextColor(self.coinTable.item(rowIndex, 2), resultDict['change_rate'])
        self.coinTable.item(rowIndex, 3).setText(str(resultDict['acc_trade_price']))

    def requestMarketCode(self):
        url = "https://api.upbit.com/v1/market/all"
        querystring = {"isDetails": "true"}
        headers = {"Accept": "application/json"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.text)
        self.resultMarketCode(result)

    def resultMarketCode(self, result):
        for v in result:
            if 'KRW' in str(v['market']):
                marketCode = v['market']
                koreanName = v['korean_name']
                marketWarning = v['market_warning']

                self.coinNameDict[koreanName] = {'market_warning': marketWarning, 'market_code': marketCode}
                self.marketCodeDict[marketCode] = {'market_warning': marketWarning, 'korean_name': koreanName}

    def addRow(self, text):
        coinInfo = self.getCoinInfo(text)
        coinName = coinInfo['coin_name']
        marketCode = coinInfo['market_code']

        row = self.coinTable.rowCount()
        for r in range(0, row):
            if coinName == self.coinTable.item(r, 0).text():
                return

        coinNameItem = QTableWidgetItem(coinName)
        coinNameItem.setFlags(QtCore.Qt.ItemIsEnabled)

        self.coinTable.setRowCount(row + 1)

        self.coinTable.setItem(row, 0, coinNameItem)
        self.coinTable.setItem(row, 1, QTableWidgetItem(' '))
        self.coinTable.setItem(row, 2, QTableWidgetItem(' '))
        self.coinTable.setItem(row, 3, QTableWidgetItem(' '))

    def getMarketCode(self, text):
        marketCode = ''
        if self.coinNameDict.get(text) is not None:
            marketCode = self.coinNameDict[text]['market_code']
        elif self.marketCodeDict.get(text) is not None:
            marketCode = text

        return marketCode

    def getCoinInfo(self, text):
        coinName = ''
        marketCode = ''

        if self.coinNameDict.get(text) is not None:
            coinName = text
            marketCode = self.coinNameDict[text]['market_code']
        elif self.marketCodeDict.get(text) is not None:
            coinName = self.marketCodeDict[text]['korean_name']
            marketCode = text
        else:
            return

        return {'coin_name': coinName, 'market_code': marketCode}
