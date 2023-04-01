import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import requests
from PIL import Image
from io import BytesIO

from mongoDB import *


# Main Screen
class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi("MainScreen.ui", self)
        self.Sbutton.clicked.connect(self.gotoSearchScreen)
        self.Hbutton.clicked.connect(self.gotoCarInfo)
        self.quit_button.clicked.connect(self.quit_func)
        self.show()

    def gotoSearchScreen(self):
        sScreen = FilterScreen()
        widget.addWidget(sScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoCarInfo(self):
        cScreen = CarInfo()
        widget.addWidget(cScreen)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def quit_func(self):
        sys.exit(app.exec())


# Filter Screen
class FilterScreen(QMainWindow):
    def __init__(self):
        super(FilterScreen, self).__init__()
        loadUi("FilterScreen.ui", self)
        self.Hbutton.clicked.connect(self.gotoHomeScreen)
        self.quit_button.clicked.connect(self.quit_func)

        # Filter for later use(not for now)
        '''self.price_check1.setStyleSheet("QCheckBox" "{"
                                        "font-size: 25px;"
                                        "spacing:15px;"
                                        "color:white;"
                                        "font-weight:bold;"
                                        "font-family: Open Sans; "
                                        "}""QCheckBox::indicator" "{"
                                        "width:25px;"
                                        "height:25px;"
                                        "background-color:white;"
                                        "border-radius: 8px;"
                                        "}" "QCheckBox::indicator:unchecked" "{"
	                                    "background-color:red;"
                                        "}")
        '''

        # Car display(random 5, no filter)

        self.cdt.setRowCount(row_count)
        self.cdt.setColumnCount(col_count)
        self.cdt.setHorizontalHeaderLabels((records[0].keys()))

        idx = 0;
        # Adding/Showing data to the table
        for x in records:
            self.cdt.setItem(idx, 1, QtWidgets.QTableWidgetItem(x['manufacturer']))
            self.cdt.setItem(idx, 2, QtWidgets.QTableWidgetItem(x['modelName']))
            self.cdt.setItem(idx, 3, QtWidgets.QTableWidgetItem(x['vin']))
            self.cdt.setItem(idx, 4, QtWidgets.QTableWidgetItem(x['color']))
            self.cdt.setItem(idx, 5, QtWidgets.QTableWidgetItem(str(x['year'])))
            self.cdt.setItem(idx, 6, QtWidgets.QTableWidgetItem(str(x['mileage'])))
            self.cdt.setItem(idx, 7, QtWidgets.QTableWidgetItem(x['transType']))
            self.cdt.setItem(idx, 8, QtWidgets.QTableWidgetItem(str(x['price'])))
            self.cdt.setItem(idx, 9, QtWidgets.QTableWidgetItem(x['fuelType']))
            self.cdt.setItem(idx, 10, QtWidgets.QTableWidgetItem(x['image']))
            self.cdt.setItem(idx, 11, QtWidgets.QTableWidgetItem(x['url']))
            idx += 1

        

    def quit_func(self):
        sys.exit(app.exec())

    def gotoHomeScreen(self):
        hScreen = MainScreen()
        widget.addWidget(hScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)





class CarInfo(QMainWindow):
    def __init__(self):
        super(CarInfo, self).__init__()
        loadUi("CarInfo.ui", self)
        self.Hbutton.clicked.connect(self.gotoHomeScreen)
        self.quit_button.clicked.connect(self.quit_func)

        # Data

    def gotoHomeScreen(self):
        hScreen = MainScreen()
        widget.addWidget(hScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def quit_func(self):
        sys.exit(app.exec())


# Data base
records = getRecords(10)
row_count = len(records)
col_count = len(records[0])

# Create application
app = QApplication(sys.argv)
mc = MainScreen()
sc = FilterScreen()
ci = CarInfo()

# Creat widgets to stores multiple windows/screens
widget = QStackedWidget()
widget.addWidget(mc)
widget.addWidget(sc)
widget.addWidget(ci)
widget.setFixedSize(1200, 700)

# No windows bar/Status bar
widget.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
widget.show()
sys.exit(app.exec())
