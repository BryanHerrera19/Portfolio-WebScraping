# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mille\Downloads\Code\COMP_195 Senior Project\senior-project-spring-2023-web-scraping\MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bg = QtWidgets.QFrame(self.centralwidget)
        self.bg.setStyleSheet("QFrame{\n"
"    background-color: rgb(64, 26, 255);\n"
"    border-radius:8px;\n"
"}")
        self.bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bg.setObjectName("bg")
        self.quit_button = QtWidgets.QPushButton(self.bg)
        self.quit_button.setGeometry(QtCore.QRect(1159, 5, 16, 16))
        self.quit_button.setMinimumSize(QtCore.QSize(16, 16))
        self.quit_button.setMaximumSize(QtCore.QSize(16, 16))
        self.quit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quit_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255,11,68); \n"
"    border-radius: 8px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255,11,68,150); \n"
"}")
        self.quit_button.setText("")
        self.quit_button.setObjectName("quit_button")
        self.wallpaper = QtWidgets.QLabel(self.bg)
        self.wallpaper.setGeometry(QtCore.QRect(-6, 26, 1191, 645))
        self.wallpaper.setText("")
        self.wallpaper.setPixmap(QtGui.QPixmap("c:\\Users\\mille\\Downloads\\Code\\COMP_195 Senior Project\\senior-project-spring-2023-web-scraping\\bg.png"))
        self.wallpaper.setScaledContents(True)
        self.wallpaper.setObjectName("wallpaper")
        self.GSbutton = QtWidgets.QPushButton(self.bg)
        self.GSbutton.setGeometry(QtCore.QRect(240, 440, 100, 25))
        self.GSbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GSbutton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(139,195,74);\n"
"    border-radius:8px;\n"
"    color:white; \n"
"    font-family: Open Sans;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(139,195,74,150);\n"
"}")
        self.GSbutton.setObjectName("GSbutton")
        self.title1 = QtWidgets.QLabel(self.bg)
        self.title1.setGeometry(QtCore.QRect(240, 280, 141, 31))
        self.title1.setStyleSheet("QLabel {\n"
"    background-color: rgba(0,0,0,0);\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color:white;\n"
"}")
        self.title1.setObjectName("title1")
        self.label = QtWidgets.QLabel(self.bg)
        self.label.setGeometry(QtCore.QRect(230, 290, 331, 141))
        self.label.setStyleSheet("QLabel{\n"
"    background-color: rgb(0,0,0,0);\n"
"    font-size: 150px; \n"
"    font-weight: bold; \n"
"    font-family: Segoe Print;\n"
"    color: white;\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.bg)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GSbutton.setText(_translate("MainWindow", "Get Started"))
        self.title1.setText(_translate("MainWindow", "Welcome to "))
        self.label.setText(_translate("MainWindow", "UCR"))