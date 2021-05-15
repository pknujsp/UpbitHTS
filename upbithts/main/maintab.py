import json
import sys
import pyupbit
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, Qt

from upbithts.main import customcoinlistitem


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

        self.coinListWidget = QListWidget(self)
        self.coinInfoView = QFrame()
        self.coinInfoView.setFrameShape(QFrame.Box)

        self.coinViewsBox = QHBoxLayout()
        self.coinViewsBox.addWidget(self.coinListWidget, 3)
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
        self.addListItem(text)
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
        myQCustomQWidget = None
        for row in range(0, self.coinListWidget.count()):
            myQCustomQWidget = self.coinListWidget.itemWidget(self.coinListWidget.item(row))
            if coinName == myQCustomQWidget.coinName:
                break

        resultDict = result[0]
        myQCustomQWidget.setData(resultDict['trade_price'],
                                 resultDict['change_rate'], resultDict['change_price'],
                                 resultDict['acc_trade_price'])

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

    def addListItem(self, text):
        coinInfo = self.getCoinInfo(text)
        coinName = coinInfo['coin_name']
        marketCode = coinInfo['market_code']

        for row in range(0, self.coinListWidget.count()):
            if coinName == self.coinListWidget.item(row).data(10):
                return

        qWidget = customcoinlistitem.CustomCoinListItemWidget(coinName=coinName, marketCode=marketCode)

        qListWidgetItem = QListWidgetItem(self.coinListWidget)
        qListWidgetItem.setSizeHint(qWidget.sizeHint())

        qListWidgetItem.setData(10, coinName)
        self.coinListWidget.addItem(qListWidgetItem)
        self.coinListWidget.setItemWidget(qListWidgetItem, qWidget)

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
