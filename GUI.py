import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap
import requests

from PyQt5 import *

from mongoDB import *

            
# Main Screen
class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi("MainScreen.ui", self)
        self.GSbutton.clicked.connect(self.gotoSearchScreen)
        self.quit_button.clicked.connect(self.quit_func)
        # self.show()

    def gotoSearchScreen(self):
        # widget.setCurrentWidget(sc)
        sc = FilterScreen()
        widget.addWidget(sc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def quit_func(self):
        sys.exit(app.exec())


# Filter Screen
class FilterScreen(QMainWindow):
    def __init__(self):
        super(FilterScreen, self).__init__()
        loadUi("filter.ui", self)
        # Go to home screen
        self.button_refresh.clicked.connect(self.refreshing_page)
        self.button_home.clicked.connect(self.gotoHomeScreen)
        self.button_quit.clicked.connect(self.quit_func)

        # Set Icon for buttons
        self.button_filter.setIcon(QtGui.QIcon("filter.png"))
        self.button_search.setIcon(QtGui.QIcon("search.png"))
        self.button_refresh.setIcon(QtGui.QIcon("refresh.png"))
        self.button_update.setIcon(QtGui.QIcon("package.png"))

        # Linked value to the slider
        self.slider_price.valueChanged.connect(self.price_change)
        self.slider_miles.valueChanged.connect(self.mile_change)
        self.button_filter.clicked.connect(self.show_filter)
        #self.button_update.clicked.connect(self.show_filter1)
        self.button_update.clicked.connect(self.show_filter2)
        self.button_search.clicked.connect(self.search)

        self.pasteCars(5, None)

        self.cdt.cellClicked.connect(self.gotoCarInfo)

    def search(self):
        years = []
        manufacturers = []
        for x in self.buttonGroup.buttons():
            years.append(x.text())
        for x in self.buttonGroup_2.buttons():
            manufacturers.append(x.text().upper())
    
        search_text = self.search_bar.text().upper()
        tempList = querySearchText(years, manufacturers, search_text)
        self.pasteCars(len(tempList), tempList)



    # Text for price slider
    def price_change(self):
        num_price = str(self.slider_price.value())
        self.price_label.setText(num_price)

    # Text for mile slider
    def mile_change(self):
        num_mile = str(self.slider_miles.value())
        self.mile_label.setText(num_mile)

    # Side filter animation

    def show_filter1(self):
        cdt_width = self.cdt.width()


        # For slide in and out
        if cdt_width == 1165:
            new_cdt_width = 0

        else:
            new_cdt_width = 1165



        # Animation
        self.animation = QPropertyAnimation(self.cdt, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(cdt_width)
        self.animation.setEndValue(new_cdt_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def show_filter2(self):
        inven_width = self.inventory.width()

        # For slide in and out
        if inven_width == 0:
            new_inven_width = 1165
        else:
            new_inven_width = 0


        # Animation
        self.animation = QPropertyAnimation(self.inventory, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(inven_width)
        self.animation.setEndValue(new_inven_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InBack)
        self.animation.start()
    def show_filter(self):
        width = self.left_main_frame.width()

        # For slide in and out
        if width == 0:
            newWidth = 285
        else:
            newWidth = 0


        # Animation
        self.animation = QPropertyAnimation(self.left_main_frame, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


        # Enable filter
        try:
            self.button_submit.disconnect()
            self.button_search.disconnect()
        except:
            pass
        self.button_search.clicked.connect(lambda: self.search())
        self.button_submit.clicked.connect(lambda: self.filterChange())
    
    #Pastes cars onto a table to view
    def pasteCars(self, startVal, queriedList):
        self.cdt.setRowCount(0)
        if(queriedList == None):
            self.records = getRecordLimit(startVal)
        else:
            self.records = queriedList

        row_count = len(self.records)
        col_count = 7

        # Setting the number of rows and cols
        self.cdt.setRowCount(row_count)
        self.cdt.setColumnCount(col_count)

        self.cdt.setHorizontalHeaderLabels(['Images','Manufacturer','Model Name','Year','Mileage','Price','Fuel Type'])

        idx = 0;
        # Adding/Showing data to the table
        for x in self.records:

            r = requests.get(x['image'],stream=True)
            assert r.status_code == 200
            
            pix = QPixmap()
            pix.loadFromData(r.content)
            
            w = QLabel()
            w.setPixmap(pix.scaled(400,300,Qt.KeepAspectRatio))
            
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
    def filterChange(self):
        if(self.buttonGroup_2.checkedButton() == None):
            tempBrandQuery = None
        else:
            tempBrandQuery = self.buttonGroup_2.checkedButton().accessibleName()
        tempList = setPriceMileQuery(self.slider_price.value(),
                                     self.slider_miles.value(),
                                     self.buttonGroup.checkedId(),
                                     tempBrandQuery)
        self.pasteCars(len(tempList), tempList)
        
    #Quits the application
    def quit_func(self):
        sys.exit(app.exec())

    #Takes user to the homescreen
    def gotoHomeScreen(self):
        widget.setCurrentWidget(mc)

    def refreshing_page(self):
        fc = FilterScreen()
        widget.addWidget(fc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoCarInfo(self, row):
        widget.setCurrentWidget(ci) 
        
        print('clicked!', row)
        print(self.records[row])
        return ci.gotoCarInfo(row)




class CarInfo(FilterScreen):
    def __init__(self):
        super(CarInfo, self).__init__()
        loadUi("CarInfo.ui", self)
        # self.Hbutton.clicked.connect(self.gotoHomeScreen)
        self.back_button.clicked.connect(self.gotoFilter)
        self.quit_button.clicked.connect(self.quit_func)
        

        # Set Icon for buttons
        self.back_button.setIcon(QtGui.QIcon("return.png"))


    def gotoFilter(self):
        #self.lay.removeWidget(self.w)
        widget.setCurrentWidget(sc)
    def quit_func(self):
        sys.exit(app.exec())

    def gotoCarInfo(self, row):
        self.lay = QHBoxLayout(self.upper_left)
        r = requests.get(self.records[row]['image'],stream=True)
        assert r.status_code == 200
        pix = QPixmap()
        pix.loadFromData(r.content)
        self.w = QLabel()
        self.w.setPixmap(pix.scaled(576,408,Qt.KeepAspectRatio))
        self.lay.addWidget(self.w)

        self.lay1 = QVBoxLayout()

        self.manu = QLabel("Manufacturer:" + " " + self.records[row]['manufacturer'])
        self.lay1.addWidget(self.manu)

        self.mile = QLabel("Model Name:" + " " + self.records[row]['modelName'])
        self.lay1.addWidget(self.mile)

        self.year = QLabel("Year:" + " " + str(self.records[row]['year']))
        self.lay1.addWidget(self.year)

        self.color = QLabel("Color:" + " " + self.records[row]['color'])
        self.lay1.addWidget(self.color)

        self.fuel = QLabel("Fuel Type:" + " " + self.records[row]['fuelType'])
        self.lay1.addWidget(self.fuel)

        self.vin = QLabel("Vin:" + " " + self.records[row]['vin'])
        self.lay1.addWidget(self.vin)

        self.trans = QLabel("TransType:" + " " + self.records[row]['transType'])
        self.lay1.addWidget(self.trans)

        self.price = QLabel("Price:" + " " + "$" + str(self.records[row]['price']))
        self.lay1.addWidget(self.price)





        self.mile = QLabel("Miles Driven:" + " " + str(self.records[row]['mileage']))
        self.lay1.addWidget(self.mile)

        self.lower_left.setLayout(self.lay1)








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
widget.setCurrentWidget(mc)
widget.setFixedSize(1200, 700)

# No windows bar/Status bar
widget.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
widget.show()
sys.exit(app.exec())