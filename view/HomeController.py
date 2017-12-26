import sys
import cv2

from view.AboutUsController import AboutUs
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui,QtCore
from PyQt5.QtCore import Qt,QThread,pyqtSignal
from PyQt5.QtGui import QImage,QPixmap

from view.ChooseAmountController import ChooseAmount
from view.Home import Ui_MainWindow
from controller.FluxController import FluxController


class Home(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.actionChoose.triggered.connect(self.clicked_choose_event)
        self.actionQuit.triggered.connect(self.clicked_quit_event)
        self.actionAbout_Us.triggered.connect(self.clicked_aboutUs_event)

        self.pushButtonVideo.clicked.connect(self.clicked_video_file)
        self.pushButtonData.clicked.connect(self.clicked_data_file)
        self.reculer.clicked.connect(self.clicked_reculer)


    def clicked_choose_event(self):
        chooseAmount = ChooseAmount()
        chooseAmount.exec()

    def clicked_quit_event(self):
        app = QApplication(sys.argv)
        sys.exit(app.exec_())

    def clicked_aboutUs_event(self):
        aboutUs = AboutUs()
        aboutUs.exec()

    def clicked_video_file(self):
        self.videoFileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file')

    def clicked_data_file(self):
        self.dataFileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file')

    def clicked_reculer(self):
        self.fc = FluxController([],self.videoFileName[0],self.dataFileName[0])
        self.fc.openVideo()
        self.label.resize(150,150)
        self.pushButtonData.hide()
        self.pushButtonVideo.hide()
        self.label.setText(" ")
        self.th = Thread(self,self.fc.frameList)
        self.th.changePixmap.connect(self.label.setPixmap)
        self.th.start()
        # for frame in self.fc.frameList:
        #     frame = cv2.cvtColor(frame.imageMat, cv2.COLOR_BGR2RGB)
        #     img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        #     pix = QtGui.QPixmap.fromImage(img)
        #     pix = pix.scaled(150, 150, Qt.KeepAspectRatio)
        #     self.label.setPixmap(pix)


class Thread(QThread):
    changePixmap = pyqtSignal(QPixmap)

    def __init__(self,parent=None,frameList=None):
        QThread.__init__(self,parent=parent)
        self.isRunning = True
        self.frameList = frameList

    def run(self):
        for frame in self.frameList:
            frame = cv2.cvtColor(frame.imageMat, cv2.COLOR_BGR2RGB)
            img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            pix = QtGui.QPixmap.fromImage(img)
            pix = pix.scaled(150, 150, Qt.KeepAspectRatio)
            # self.label.setPixmap(pix)
            self.changePixmap.emit(pix)
            self.msleep(100)

    def stop(self):
        self.isRunning = False
        self.quit()
        self.wait()


