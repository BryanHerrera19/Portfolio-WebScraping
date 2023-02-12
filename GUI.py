import sys
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#Main screen
class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp,self).__init__()
        self.setWindowTitle("URC")
        self.setFixedSize(1300, 800)
        self.grid = QGridLayout(self)
        # Background image
        self.setStyleSheet("background-image:url(background.png);")

        # Setting Icon
        # Still need to fix the background transparency, image animation
        self.setIcon = QLabel(self)
        pixmap = QPixmap('setting.png')
        self.setIcon.setPixmap(pixmap)
        self.setIcon.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setIcon.setGeometry(1200,15,70,70)
        self.setIcon.setStyleSheet(
            "*{opacity: 0.5;" +
            "transition:1s ease;}" +
            "*:hover{opacity:1;" +
            "transition: 1s ease;}"
        )
        #self.setCentralWidget(self.label)


        #Home and Search button
        self.hbutton = QPushButton("Home", self)
        self.hbutton.setGeometry(70, 40, 130, 45)
        self.hbutton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        # Temporarily style, will change later
        self.hbutton.setStyleSheet(
            "*{background: '#8BC34A';" +
            "color:white;" +
            "font-family: Open Sans;" +
            "font-size: 30px;" +
            "border-radius: 8px;}" +
            "*:hover{background: red;}"
        )

        self.sbutton = QPushButton("Search", self)
        self.sbutton.setGeometry(230, 40, 130, 45)
        self.sbutton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        # Temporarily style, will change later
        self.sbutton.setStyleSheet(
            "*{background: '#8BC34A';" +
            "color:white;" +
            "font-family: Open Sans;" +
            "font-size: 30px;" +
            "border-radius: 8px;}" +
            "*:hover{background: red;}"
        )


        # Get started button
        self.gbutton = QPushButton("Get Started", self)
        self.gbutton.setGeometry(120,440,100,30)
        self.gbutton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.gbutton.setStyleSheet(
            "*{background: '#8BC34A';" +
            "color:white;" +
            "border-radius: 8px;}" +
            "*:hover{background: red;}"
        )



        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = MainApp()
    c.show()
    sys.exit(app.exec())


