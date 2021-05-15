def changeTextColor(self, widget, changeRate):
    changeRateFloat = float(changeRate)
    color = '''color: rgb(255, 0, 0);''' if changeRateFloat < 0.0 else '''color: rgb(0, 0, 255);'''

    widget.setStyleSheet(color)
