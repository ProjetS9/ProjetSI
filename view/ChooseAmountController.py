from PyQt5 import QtWidgets

from view.ChooseAmount import Ui_AmountDialog


class ChooseAmount(QtWidgets.QDialog, Ui_AmountDialog):

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_AmountDialog.__init__(self)
        self.setupUi(self)