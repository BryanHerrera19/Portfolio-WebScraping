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
        loadUi("filter.ui", self)
        # self.Hbutton.clicked.connect(self.gotoHomeScreen)
        self.quit_button.clicked.connect(self.quit_func)
        self.price_slider.valueChanged.connect(self.price_change)
        self.miles_slider.valueChanged.connect(self.mile_change)
        self.pasteCars(5, None)

    def price_change(self):
        num_price = str(self.price_slider.value())
        self.price_label.setText(num_price)

    def mile_change(self):
        num_mile = str(self.miles_slider.value())
        self.mile_label.setText(num_mile)

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
        self.price_check1.stateChanged.connect(self.priceChange)
        self.price_check2.stateChanged.connect(self.priceChange)
        self.price_check3.stateChanged.connect(self.priceChange)
        self.price_check4.stateChanged.connect(self.priceChange)
        self.miles_check1.stateChanged.connect(self.milesChange)
        self.miles_check2.stateChanged.connect(self.milesChange)
        self.miles_check3.stateChanged.connect(self.milesChange)
        self.miles_check4.stateChanged.connect(self.milesChange)
        self.year_check1.stateChanged.connect(self.yearChange)
        self.year_check2.stateChanged.connect(self.yearChange)
        self.year_check3.stateChanged.connect(self.yearChange)
        self.year_check4.stateChanged.connect(self.yearChange)
        self.brand_check.stateChanged.connect(self.brandChange)
        self.brand_check1.stateChanged.connect(self.brandChange)
        self.brand_check2.stateChanged.connect(self.brandChange)
        self.brand_check3.stateChanged.connect(self.brandChange)
        self.brand_check4.stateChanged.connect(self.brandChange)
        self.brand_check5.stateChanged.connect(self.brandChange)


    #Pastes cars onto a table to view
    def pasteCars(self, startVal, queriedList):
        self.cdt.setRowCount(0)
        if(queriedList == None):
            records = getRecordLimit(startVal)
        else:
            records = queriedList

        row_count = len(records)
        col_count = 7

        # Setting the number of rows and cols
        self.cdt.setRowCount(row_count)
        self.cdt.setColumnCount(col_count)

        self.cdt.setHorizontalHeaderLabels(['Images','Manufacturer','Model Name','Year','Mileage','Price','Fuel Type'])

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

            # Will have to change column names
            self.cdt.setCellWidget(idx, 0, w)
            self.cdt.setItem(idx, 1, QtWidgets.QTableWidgetItem(x['manufacturer']))
            self.cdt.setItem(idx, 2, QtWidgets.QTableWidgetItem(x['modelName']))
            self.cdt.setItem(idx, 3, QtWidgets.QTableWidgetItem(str(x['year'])))
            self.cdt.setItem(idx, 4, QtWidgets.QTableWidgetItem(str(x['mileage'])))
            self.cdt.setItem(idx, 5, QtWidgets.QTableWidgetItem(str(x['price'])))
            self.cdt.setItem(idx, 6, QtWidgets.QTableWidgetItem(x['fuelType']))
            idx += 1

        #Resizing the rows and cols to match the information
        self.cdt.resizeRowsToContents()
        self.cdt.resizeColumnsToContents()

    #Outputs the queried list from filter when clicking checkbox
    def priceChange(self):
        if(self.price_check1.checkState() == 0 or
           self.price_check2.checkState() == 0 or
           self.price_check3.checkState() == 0 or
           self.price_check4.checkState() == 0):
            self.pasteCars(5, None)
        if(self.price_check1.checkState() == 2):
            tempList = setPriceQuery(self.price_check1.accessibleName())
            self.pasteCars(len(tempList), tempList)
        if(self.price_check2.checkState() == 2):
            tempList = setPriceQuery(self.price_check2.accessibleName())
            self.pasteCars(len(tempList), tempList)
        if(self.price_check3.checkState() == 2):
            tempList = setPriceQuery(self.price_check3.accessibleName())
            self.pasteCars(len(tempList), tempList)
        if(self.price_check4.checkState() == 2):
            tempList = setPriceQuery(self.price_check4.accessibleName())
            self.pasteCars(len(tempList), tempList)

    def milesChange(self):
        if(self.miles_check1.checkState() == 0 or
           self.miles_check2.checkState() == 0 or
           self.miles_check3.checkState() == 0 or
           self.miles_check4.checkState() == 0):
            self.pasteCars(5, None)
        if(self.miles_check1.checkState() == 2):
            tempList = setMileQuery(self.miles_check1.accessibleName())
            self.pasteCars(len(tempList), tempList)
        if(self.miles_check2.checkState() == 2):
            tempList = setMileQuery(self.miles_check2.accessibleName())
            self.pasteCars(len(tempList), tempList)
        if(self.miles_check3.checkState() == 2):
            tempList = setMileQuery(self.miles_check3.accessibleName())
            self.pasteCars(len(tempList), tempList)
        if(self.miles_check4.checkState() == 2):
            tempList = setMileQuery(self.miles_check4.accessibleName())
            self.pasteCars(len(tempList), tempList)

    def yearChange(self):
        if(self.year_check1.checkState() == 0 or
           self.year_check2.checkState() == 0 or
           self.year_check3.checkState() == 0 or
           self.year_check4.checkState() == 0):
            self.pasteCars(5, None)
        if(self.year_check1.checkState() == 2):
            tempList = setYearQuery(self.year_check1.accessibleName())
            self.pasteCars(len(tempList), tempList)
        if(self.year_check2.checkState() == 2):
            tempList = setYearQuery(self.year_check2.accessibleName())
            self.pasteCars(len(tempList), tempList)
        if(self.year_check3.checkState() == 2):
            tempList = setYearQuery(self.year_check3.accessibleName())
            self.pasteCars(len(tempList), tempList)
        if(self.year_check4.checkState() == 2):
            tempList = setYearQuery(self.year_check4.accessibleName())
            self.pasteCars(len(tempList), tempList)

    def brandChange(self):
        if(self.brand_check.checkState() == 0 or
           self.brand_check1.checkState() == 0 or
           self.brand_check2.checkState() == 0 or
           self.brand_check3.checkState() == 0 or
           self.brand_check4.checkState() == 0 or
           self.brand_check5.checkState() == 0):
            self.pasteCars(5, None)
        if(self.brand_check.checkState() == 2):
            tempList = setBrandQuery(self.brand_check.accessibleName())
            self.pasteCars(len(tempList), tempList)
        if(self.brand_check1.checkState() == 2):
            tempList = setBrandQuery(self.brand_check1.accessibleName())
            self.pasteCars(len(tempList), tempList)
        if(self.brand_check2.checkState() == 2):
            tempList = setBrandQuery(self.brand_check2.accessibleName())
            self.pasteCars(len(tempList), tempList)
        if(self.brand_check3.checkState() == 2):
            tempList = setBrandQuery(self.brand_check3.accessibleName())
            self.pasteCars(len(tempList), tempList)
        if(self.brand_check4.checkState() == 2):
            tempList = setBrandQuery(self.brand_check4.accessibleName())
            self.pasteCars(len(tempList), tempList)
        if(self.brand_check5.checkState() == 2):
            tempList = setBrandQuery(self.brand_check5.accessibleName())
            self.pasteCars(len(tempList), tempList)
        
    #Quits the application
    def quit_func(self):
        sys.exit(app.exec())

    #Takes user to the homescreen
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