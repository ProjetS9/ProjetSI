class Frame:
    def __init__(self,idFrame,imageMat,rectangle):
        self.idFrame = idFrame
        self.imageMat = imageMat
        self.rectangle = rectangle
    def __init__(self,idFrame,imageMat):
        self.idFrame = idFrame
        self.imageMat = imageMat
        self.rectangle = []
    def setRectangle(self,data):
        self.rectangle.append(data)