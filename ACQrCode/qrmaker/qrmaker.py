import pyqrcode
from extra_tools import fileNamer

class QrController():
    qr = None

    def buildQr(self, data: str):
        self.qr = pyqrcode.create(data, error='L', mode='binary')
        return self

    def saveAsPNG(self, outputPath = "", object = None):
        self.qr.png(fileNamer(outputPath, 'png'), scale=5)
        return self

    def saveAsSVG(self, outputPath = "", object = None):
        self.qr.svg(fileNamer(outputPath, 'svg'), scale=5)
        return self