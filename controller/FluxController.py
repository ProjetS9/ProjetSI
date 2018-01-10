import cv2
import numpy as np
import random

import sys
sys.path.append("..")
from model.Frame import Frame
from model.Data import Data

class FluxController:
    def __init__(self,frameList,nomFichierVideo,nomFichierData):
        self.frameList = frameList
        self.nomFichierVideo = nomFichierVideo
        self.nomFichierData = nomFichierData

    def openVideo(self):
        self.cap = cv2.VideoCapture(self.nomFichierVideo)
        i = 1
        while (True):
            ret, fra = self.cap.read()
            if ret == True:
                i = i + 1
                frame = Frame(i, fra)
                self.frameList.append(frame)
            else:
                break

        if self.nomFichierData != "":
            for line in open(self.nomFichierData):
                if line.startswith("Frame"):
                    f, idFrame = line.split("	")
                    idFrame = int(idFrame)
                else:
                    idObj, top, left, bottom, right = line.split("\t")
                    idObj = int(idObj)
                    top = int(top)
                    bottom = int(bottom)
                    left = int(left)
                    right = int(right)
                    data = Data(idObj, top, bottom, left, right)
                    for frame in self.frameList:
                        if frame.idFrame == idFrame:
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

        for frame in self.frameList:
            result, frame.imageMat = cv2.imencode('.jpg', frame.imageMat,[int(cv2.IMWRITE_JPEG_QUALITY), 95])
            img_code = np.array(frame.imageMat)
            img_data = img_code.tostring()
            frame.imageMat = img_data


    # show every frame of the video
    def showVideo(self,frame):
        frame.imageMat = cv2.imdecode(np.fromstring(frame.imageMat,dtype='uint8'),1)
        cv2.imshow("Suivi",frame.imageMat)
        cv2.waitKey(1)
        # for frame in self.frameList:
        #     cv2.imshow("Suivi", frame.imageMat)
        #     cv2.waitKey(1)

    def readFrame(self,currentFrameNumber):
        frame = self.frameList[currentFrameNumber - 1]
        return frame

    def nextFrame(self,currentFrameNumber):
        return self.frameList[currentFrameNumber]

    def previousFrame(self,currentFrameNumber):
        return self.frameList[currentFrameNumber - 2]

# fc = FluxController([],'v1.avi','View1.txt')
# fc.openVideo()
# # currentId = 1
# # frame = fc.readFrame(currentId)
# # fc.showVideo(frame)
# # print(len(fc.frameList))
# for frame in fc.frameList:
#     fc.showVideo(frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break





