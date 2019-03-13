from PIL import Image
from pyzbar import pyzbar as pb
import json

class QReader():

    def extractQr(self, path: str):
        data = pb.decode(Image.open(path))
        return data

    def readAndDecodeQr(self, path: str):
        data = self.extractQr(path)
        return data[0].data.decode('utf-8')

    def jsonifyQr(self, path: str):
        data = self.readAndDecodeQr(path)
        return json.loads(data)