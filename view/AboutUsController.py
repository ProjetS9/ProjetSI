from PyQt5 import QtWidgets

from view.AboutUs import Ui_AboutUs


class AboutUs(QtWidgets.QDialog, Ui_AboutUs):

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_AboutUs.__init__(self)
        self.setupUi(self)