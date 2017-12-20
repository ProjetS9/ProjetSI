import cv2
import os
import numpy as np
import random
class Data:
    def __init__(self,idObj,top,bottom,left,right):
        self.idObj=idObj
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

class Frame:
    def __init__(self,idFrame,imageMat,rectangle):
        self.idFrame=idFrame
        self.imageMat=imageMat
        self.rectangle = rectangle
    def __init__(self,idFrame,imageMat):
        self.idFrame=idFrame
        self.imageMat=imageMat
        self.rectangle=[]
    def setRectangle(self,data):
        self.rectangle.append(data)

class SequenceController:
    def __init__(self,frameList,nomFichierVideo,nomFichierData):
        self.frameList=frameList
        self.nomFichierVideo=nomFichierVideo
        self.nomFichierData=nomFichierData

    def openVedio(self):
        files = os.listdir(self.nomFichierVideo)
        i = 1
        for file in files:
            image = cv2.imread(self.nomFichierVideo + '/'+ file)
            frame = Frame(i,image)
            self.frameList.append(frame)
            i=i+1
        for line in open(self.nomFichierData):
            if line.startswith("Frame"):
                f,idFrame=line.split("	")
                idFrame = int(idFrame)
            else:
                idObj, top, left,bottom,right=line.split("\t")
                idObj=int(idObj)
                top=int(top)
                bottom=int(bottom)
                left=int(left)
                right=int(right)
                data=Data(idObj,top,bottom,left,right)
                for frame in self.frameList:
                    if frame.idFrame==idFrame:
                        frame.setRectangle(data)
        maxId = 0
        for frame in self.frameList:
            for data in frame.rectangle:
                if data.idObj > maxId:
                    maxId = data.idObj
        colorList = []

        for i in range(0, maxId):
            color = []
            for j in range(0, 3):
                color.append(random.randint(0, 255))
            colorList.append(color)

        for frame in self.frameList:
            if len(frame.rectangle)!=0:
                for data in frame.rectangle:
                    idObj = data.idObj
                    top=data.top-1
                    left=data.left-1
                    bottom=data.bottom-1
                    right=data.right-1
                    if top >= np.shape(frame.imageMat)[0]:
                        top = np.shape(frame.imageMat)[0] - 1
                    if bottom >= np.shape(frame.imageMat)[0]:
                        bottom = np.shape(frame.imageMat)[0] - 1
                    if left >= np.shape(frame.imageMat)[1]:
                        left = np.shape(frame.imageMat)[1] - 1
                    if right >= np.shape(frame.imageMat)[1]:
                        right = np.shape(frame.imageMat)[1] - 1

                    while top < bottom:
                        frame.imageMat[top][left][0]= colorList[idObj - 1][0]
                        frame.imageMat[top][right][0]= colorList[idObj - 1][0]
                        frame.imageMat[top][left][1] = colorList[idObj - 1][1]
                        frame.imageMat[top][right][1] = colorList[idObj - 1][1]
                        frame.imageMat[top][left][2] = colorList[idObj - 1][2]
                        frame.imageMat[top][right][2] = colorList[idObj - 1][2]
                        top=top+1

                    top = data.top-1
                    if top >= np.shape(frame.imageMat)[0]:
                        top = np.shape(frame.imageMat)[0] - 1
                    while left < right:
                        frame.imageMat[top][left][0]= colorList[idObj - 1][0]
                        frame.imageMat[bottom][left][0]= colorList[idObj - 1][0]
                        frame.imageMat[top][left][1]=colorList[idObj - 1][1]
                        frame.imageMat[bottom][left][1]=colorList[idObj - 1][1]
                        frame.imageMat[top][left][2]=colorList[idObj - 1][2]
                        frame.imageMat[bottom][left][2]=colorList[idObj - 1][2]
                        left=left+1

    def showVedio(self, frame):
        cv2.imshow("Suivi", frame.imageMat)
        cv2.waitKey(1)
        # for frame in self.frameList:
        #     cv2.imshow("Suivi",frame.imageMat)
        #     cv2.waitKey(1)

    def readFrame(self,currentFrameNumber):
        frame = self.frameList[currentFrameNumber-1]
        return frame

    def nextFrame(self,currentFrameNumber):
        return self.frameList[currentFrameNumber]

    def previousFrame(self,currentFrameNumber):
        return self.frameList[currentFrameNumber-2]


# sc = SequenceController([], "G:/View_001","G:/gtS2_L1_12-34_View001.txt")
# sc.openVedio()
# currentId = 1
# frame = sc.readFrame(currentId)
# sc.showVedio(frame)
# for i in range(0,800):
#     if i < 500:
#         frame = sc.nextFrame(currentId)
#         currentId += 1
#         sc.showVedio(frame)
#     else:
#         frame = sc.previousFrame(currentId)
#         currentId -= 1
#         sc.showVedio(frame)