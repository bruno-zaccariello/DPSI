Para utilzar o módulo, favor instalar as dependencias no requirements.txt

Nesse módulo você irá usar basicamente o manager.py, ele automatiza as tarefas de gerar QRCodes.

Para fins da AC foi criado um arquivo example.py para mostrar as funcionalidades em ação.

Atualmente temos 4 funções dentro do manager.py na classe QrManager:
    - newQrPNG(dados, path)
        essa função recebe dados e um caminho (opcional) e irá gerar um QR Code em PNG no caminho informado,
        caso nenhum caminho seja informado o padrão é gerar uma pasta output onde a função foi chamada

    - newQrSVG(dados, path)
        basicamente igual ao newQrPNG porém irá gerar um SVG
    
    - decodeQr(path)
        recebe um caminho de uma imagem QRCode e decodifica ela, retornando os dados brutos em string

    - jsonifyQr(path)
        recebe um caminho de uma imagem QRCode e decodifica ela em json.

- Bruno Z. 1700604