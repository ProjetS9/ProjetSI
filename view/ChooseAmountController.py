from ChooseAmount import Ui_AmountDialog
from PyQt5 import QtWidgets


class ChooseAmount(QtWidgets.QDialog, Ui_AmountDialog):

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_AmountDialog.__init__(self)
        self.setupUi(self)