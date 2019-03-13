import datetime
from pathlib import PurePath, Path

def cleanPath(path):
    pathSplit = path.split('/')
    folderPath = pathSplit[:-1]
    fileName = pathSplit[-1]
    return ''.join(x for x in folderPath), fileName

def fileNamer(path: str = "", saveAs: str = ""):
    date = datetime.datetime.now()
    if path != "":
        folderPath, fileName = cleanPath(path)
        Path(folderPath).mkdir(exist_ok=True)
        return PurePath(f'{path}.{saveAs}')
    Path('./output').mkdir(exist_ok=True)
    return PurePath(f'./output/{date.year}_{date.month}_{date.day}_{date.minute}{date.second}.{saveAs}')