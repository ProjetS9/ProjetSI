# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(420, 30, 341, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.fermer = QtWidgets.QPushButton(self.centralwidget)
        self.fermer.setGeometry(QtCore.QRect(490, 420, 60, 60))
        self.fermer.setStyleSheet("border-image: url(:/Images/arreter.png);")
        self.fermer.setText("")
        self.fermer.setObjectName("fermer")
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(560, 420, 60, 60))
        self.pause.setStyleSheet("border-image: url(:/Images/pause.png);")
        self.pause.setText("")
        self.pause.setObjectName("pause")
        self.avancer = QtWidgets.QPushButton(self.centralwidget)
        self.avancer.setGeometry(QtCore.QRect(630, 420, 60, 60))
        self.avancer.setStyleSheet("border-image: url(:/Images/avancer.png);")
        self.avancer.setText("")
        self.avancer.setObjectName("avancer")
        self.recommencer = QtWidgets.QPushButton(self.centralwidget)
        self.recommencer.setGeometry(QtCore.QRect(700, 420, 60, 60))
        self.recommencer.setStyleSheet("border-image: url(:/Images/recommencer.png);")
        self.recommencer.setText("")
        self.recommencer.setObjectName("recommencer")
        self.reculer = QtWidgets.QPushButton(self.centralwidget)
        self.reculer.setGeometry(QtCore.QRect(420, 420, 60, 60))
        self.reculer.setStyleSheet("border-image: url(:/Images/reculer.png);")
        self.reculer.setText("")
        self.reculer.setObjectName("reculer")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 30, 361, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.gridLayout.addWidget(self.graphicsView_4, 0, 1, 1, 1)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout.addWidget(self.graphicsView_3, 0, 0, 1, 1)
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.gridLayout.addWidget(self.graphicsView_5, 1, 1, 1, 1)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 1, 0, 1, 1)
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.gridLayout.addWidget(self.graphicsView_6, 3, 0, 1, 1)
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.gridLayout.addWidget(self.graphicsView_7, 2, 0, 1, 1)
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.gridLayout.addWidget(self.graphicsView_8, 2, 1, 1, 1)
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.gridLayout.addWidget(self.graphicsView_9, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionChoose = QtWidgets.QAction(MainWindow)
        self.actionChoose.setObjectName("actionChoose")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.menuFile.addAction(self.actionChoose)
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionAbout_Us)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionChoose.setText(_translate("MainWindow", "Choose"))
        self.actionQuit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))

import images_rc
