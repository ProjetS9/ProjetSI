# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChooseAmount.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AmountDialog(object):
    def setupUi(self, AmountDialog):
        AmountDialog.setObjectName("AmountDialog")
        AmountDialog.resize(400, 200)
        self.AmountLabel = QtWidgets.QLabel(AmountDialog)
        self.AmountLabel.setGeometry(QtCore.QRect(30, 60, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.AmountLabel.setFont(font)
        self.AmountLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.AmountLabel.setMouseTracking(False)
        self.AmountLabel.setObjectName("AmountLabel")
        self.AmountSpinBox = QtWidgets.QSpinBox(AmountDialog)
        self.AmountSpinBox.setGeometry(QtCore.QRect(270, 60, 100, 35))
        self.AmountSpinBox.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.AmountSpinBox.setMinimum(1)
        self.AmountSpinBox.setMaximum(8)
        self.AmountSpinBox.setObjectName("AmountSpinBox")
        self.AmountButtonBox = QtWidgets.QDialogButtonBox(AmountDialog)
        self.AmountButtonBox.setGeometry(QtCore.QRect(30, 140, 341, 32))
        self.AmountButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.AmountButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.AmountButtonBox.setObjectName("AmountButtonBox")

        self.retranslateUi(AmountDialog)
        QtCore.QMetaObject.connectSlotsByName(AmountDialog)

    def retranslateUi(self, AmountDialog):
        _translate = QtCore.QCoreApplication.translate
        AmountDialog.setWindowTitle(_translate("AmountDialog", "Choose amount of video windows"))
        self.AmountLabel.setText(_translate("AmountDialog", "Amount of video windows"))

