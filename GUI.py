import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from mongoDB import *
# Main Screen
class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen,self).__init__()
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

    def quit_func(self):
        sys.exit(app.exec())

    def gotoHomeScreen(self):
        hScreen = MainScreen()
        widget.addWidget(hScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CarInfo(QMainWindow):
    def __init__(self):
        super(CarInfo, self).__init__()
        loadUi("CarInfo.ui",self)
        self.Hbutton.clicked.connect(self.gotoHomeScreen)
        self.quit_button.clicked.connect(self.quit_func)

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
widget.setFixedSize(1200,700)

# No windows bar/Status bar
widget.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
widget.show()
sys.exit(app.exec())






