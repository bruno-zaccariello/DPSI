from manager import QRManager

qManager = QRManager()
print(qManager.newQrPNG('{"cliente": "marcos", "saldo":"15 reais"}', 'output/marcos'))
json = qManager.jsonifyQr('output/marcos.png')
print(json)
print(json.get('cliente', 'error'))