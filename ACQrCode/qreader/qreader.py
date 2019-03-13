from PIL import Image
from pyzbar import pyzbar as pb
import json

class QReader():

    def extractQr(self, path: str):
        try:
            data = pb.decode(Image.open(path))
            return data
        except:
            raise Exception('Não foi possível ler imagem Qr, ela é realmente válida ou o path está certo ?')

    def readAndDecodeQr(self, path: str):
        try:
            data = self.extractQr(path)
            return data[0].data.decode('utf-8')
        except:
            raise Exception('Não foi possível decodificar Qr')

    def jsonifyQr(self, path: str):
        data = self.readAndDecodeQr(path)
        try:
            return json.loads(data)
        except:
            print('Não foi possível transformar em json, retornando string...')
            return data