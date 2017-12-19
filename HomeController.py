from Home import Ui_MainWindow
from PyQt5 import QtWidgets
from ChooseAmountController import ChooseAmount
from AboutUsController import AboutUs
from PyQt5.QtWidgets import QApplication
import sys

class Home(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.actionChoose.triggered.connect(self.clicked_choose_event)
        self.actionQuit.triggered.connect(self.clicked_quit_event)
        self.actionAbout_Us.triggered.connect(self.clicked_aboutUs_event)



    def clicked_choose_event(self):
        chooseAmount = ChooseAmount()
        chooseAmount.exec()

    def clicked_quit_event(self):
        app = QApplication(sys.argv)
        sys.exit(app.exec_())

    def clicked_aboutUs_event(self):
        aboutUs = AboutUs()
        aboutUs.exec()