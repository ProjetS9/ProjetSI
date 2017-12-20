import cv2
import os
import time
import numpy as np
# frameList
# nomFichierVideo
# nomFichierData
# nextFrame
# previousFrame
# openVideo
# readFrame
# showVideo
class Data:
    def __init__(self,idObj,top,bottom,left,right):
        self.idObj=idObj
        self.top=top
        self.bottom=bottom
        self.left=left
        self.right=right
class Frame(Data):
    def __init__(self,idFrame,imageMat,rectangle):
        self.idFrame=idFrame
        self.imageMat=imageMat
        rectangle=rectangle
class SequenceController:
    def __init__(self,frameList,nomFichierVideo,nomFichierData):
        self.frameList=frameList
        self.nomFichierVideo=nomFichierVideo
        self.nomFichierData=nomFichierData
    def openVedio(self):
        # path = "G:/View_001"
        files = os.listdir(self.nomFichierVideo)
        for file in files:
            image = cv2.imread(self.nomFichierVideo + '/'+ file)
            self.frameList.append(image)

    def showVedio(self):
        for frame in self.frameList:
            cv2.imshow("Suivi",frame)
            cv2.waitKey(1)
    # def readFrame(self,currentFrameNumber):


frameList = []
sc = SequenceController(frameList, "G:/View_001",' ')
sc.openVedio()
sc.showVedio()


