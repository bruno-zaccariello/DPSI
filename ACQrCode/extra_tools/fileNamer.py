import datetime

def fileNamer(path: str = "", saveAs: str = ""):
    date = datetime.datetime.now()
    date_string = f'./output/{date.year}_{date.month}_{date.day}_{date.minute}{date.second}.{saveAs}'
    if path:
        return f'{path}'
    return date_string