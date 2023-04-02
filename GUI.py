import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap
import requests
from PIL import Image
from io import BytesIO
from PyQt5 import *

from mongoDB import *


# Main Screen
class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi("MainScreen.ui", self)
        # self.Sbutton.clicked.connect(self.gotoSearchScreen)
        # self.Hbutton.clicked.connect(self.gotoCarInfo)
        self.GSbutton.clicked.connect(self.gotoSearchScreen)
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
        # self.Hbutton.clicked.connect(self.gotoHomeScreen)
        self.quit_button.clicked.connect(self.quit_func)

        self.printTest()

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

    def printTest(self):
        self.cdt.setRowCount(0)
        records = getRecordLimit(5)
        row_count = len(records)
        col_count = 7

        # Setting the number of rows and cols
        self.cdt.setRowCount(row_count)
        self.cdt.setColumnCount(col_count)

        self.cdt.setHorizontalHeaderLabels(['Images','Manufacturer','Model Name','Year','Price','Mileage','Fuel Type'])

        idx = 0;
        # Adding/Showing data to the table
        for x in records:
            r = requests.get(x['image'],stream=True)
            assert r.status_code == 200
            img = QImage()
            assert img.loadFromData(r.content)
            pixel_img = img.scaled(160,120,Qt.KeepAspectRatio)
            w = QLabel()
            w.setPixmap(QPixmap(pixel_img))

            # will have to change column names
            self.cdt.setCellWidget(idx, 0, w)
            self.cdt.setItem(idx, 1, QtWidgets.QTableWidgetItem(x['manufacturer']))
            self.cdt.setItem(idx, 2, QtWidgets.QTableWidgetItem(x['modelName']))
            self.cdt.setItem(idx, 3, QtWidgets.QTableWidgetItem(str(x['year'])))
            self.cdt.setItem(idx, 4, QtWidgets.QTableWidgetItem(str(x['price'])))
            self.cdt.setItem(idx, 5, QtWidgets.QTableWidgetItem(str(x['mileage'])))
            self.cdt.setItem(idx, 6, QtWidgets.QTableWidgetItem(x['fuelType']))
            idx += 1

        #Resizing the rows and cols to match the information
        self.cdt.resizeRowsToContents()
        self.cdt.resizeColumnsToContents()
        
        
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
        # self.Hbutton.clicked.connect(self.gotoHomeScreen)
        self.quit_button.clicked.connect(self.quit_func)

        # Data

    def gotoHomeScreen(self):
        hScreen = MainScreen()
        widget.addWidget(hScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def quit_func(self):
        sys.exit(app.exec())

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
