from qrmaker import QrController
from qreader import QReader

class QRManager():
    QControl = QrController()
    QRead = QReader()

    def newQrPNG(self, data: str, file_name: str = ""):
        qrObject = self.QControl.buildQr(data).saveAsPNG(file_name)
        return self

    def newQrSVG(self, data: str, file_name: str = ""):
        qrObject = self.QControl.buildQr(data).saveAsSVG(file_name)
        return self

    def decodeQr(self, path):
        data = self.QRead.readAndDecodeQr(path)
        return data

    def jsonifyQr(self, path):
        return self.QRead.jsonifyQr(path)