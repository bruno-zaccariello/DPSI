from qrmaker import QrController as Qr

def newQrPNG(data: str, file_name: str = ""):
    QR = Qr()
    qrObject = QR.buildQr(data).saveAsPNG(file_name)

def newQrSVG(data: str, file_name: str = ""):
    QR = Qr()
    qrObject = QR.buildQr(data).saveAsSVG(file_name)

newQrPNG('love of my life')
newQrSVG('https://google.com.br')