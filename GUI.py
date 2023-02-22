import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# Main Screen
class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen,self).__init__()
        loadUi("MainScreen.ui", self)
        self.Sbutton.clicked.connect(self.gotoSearchScreen)
        self.quit_button.clicked.connect(self.quit_func)
        self.show()

    def gotoSearchScreen(self):
        sScreen = FilterScreen()
        widget.addWidget(sScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def quit_func(self):
        sys.exit(app.exec())


# Filter Screen
class FilterScreen(QMainWindow):
    def __init__(self):
        super(FilterScreen, self).__init__()
        loadUi("FilterScreen.ui", self)
        self.quit_button.clicked.connect(self.quit_func)

    def quit_func(self):
        sys.exit(app.exec())

# Create application
app = QApplication(sys.argv)
mc = MainScreen()
sc = FilterScreen()

# Creat widgets to stores multiple windows/screens
widget = QStackedWidget()
widget.addWidget(mc)
widget.addWidget(sc)
widget.setFixedSize(1200,700)

# No windows bar/Status bar
widget.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
widget.show()
sys.exit(app.exec())






