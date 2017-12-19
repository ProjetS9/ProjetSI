from AboutUs import Ui_AboutUs
from PyQt5 import QtWidgets


class AboutUs(QtWidgets.QDialog, Ui_AboutUs):

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_AboutUs.__init__(self)
        self.setupUi(self)