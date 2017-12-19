# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutUs.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutUs(object):
    def setupUi(self, AboutUs):
        AboutUs.setObjectName("AboutUs")
        AboutUs.resize(400, 300)
        self.logoLabel = QtWidgets.QLabel(AboutUs)
        self.logoLabel.setGeometry(QtCore.QRect(1, 10, 401, 131))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("Images/polytech.png"))
        self.logoLabel.setObjectName("logoLabel")
        self.versionLabel = QtWidgets.QLabel(AboutUs)
        self.versionLabel.setGeometry(QtCore.QRect(160, 170, 121, 18))
        self.versionLabel.setObjectName("versionLabel")
        self.developpeurLabel = QtWidgets.QLabel(AboutUs)
        self.developpeurLabel.setGeometry(QtCore.QRect(30, 210, 331, 51))
        self.developpeurLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.developpeurLabel.setTextFormat(QtCore.Qt.AutoText)
        self.developpeurLabel.setScaledContents(True)
        self.developpeurLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.developpeurLabel.setWordWrap(True)
        self.developpeurLabel.setObjectName("developpeurLabel")

        self.retranslateUi(AboutUs)
        QtCore.QMetaObject.connectSlotsByName(AboutUs)

    def retranslateUi(self, AboutUs):
        _translate = QtCore.QCoreApplication.translate
        AboutUs.setWindowTitle(_translate("AboutUs", "About Us"))
        self.versionLabel.setText(_translate("AboutUs", "Version: 1.0"))
        self.developpeurLabel.setText(_translate("AboutUs", "Developpeurs: BI Peng & ZENG Kai & LI Yi & XU Jiaoqiang & WANG Rujia & DAI Yuexin"))

