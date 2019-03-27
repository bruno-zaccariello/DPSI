import requests as r
from config import SEARCH_URL, DEFAULT_SEARCH_PART

FILTERS = ['forContentOwner', 'forMine', 'relatedToVideoId']

OPT_PARAMS_HELPER = {
    'channelId': 'string',
    'channelType': ['any', 'show'],
    'eventType': ['completed', 'live', 'upcoming'],
    'maxResults': 'Integer (0-50)',  # Max. value = 50
    'onBehalfOfContentOwner': 'string',  # OAuth key
    'order': ['date', 'rating', 'relevance', 'title', 'videoCount', 'viewCount'],
    'pageToken': 'string',
    'publishedAfter': 'string',  # Datetime Object (iso formatted)
    'publishedBefore': 'string',  # Datetime Object (iso formatted)
    'q': 'string',
    'regionCode': 'string',  # ISO 3166-1 Alpha 2
    'safeSearch': ['moderate', 'none', 'strict'],
    'type': ['channel', 'playlist', 'video'],
    'videoCaption': ['any', 'closedCaption', 'none'],
    'videoCategoryId': 'string',
    'videoDefinition': ['any', 'high', 'standard'],
    'videoDimension': ['any', '2d', '3d'],
    'videoDuration': ['any', 'short', 'medium', 'long'],
    'videoEmbeddable': ['any', 'true'],
    'videoType': ['any', 'episode', 'movie']
}

VALID_PARAMS = OPT_PARAMS_HELPER.keys()

class Search():
    def __init__(self, apiKey):
        self.URL = f'{SEARCH_URL}?key={apiKey}'
        self.part = DEFAULT_SEARCH_PART
        self.params = dict()

    # Add a param
    def addParam(self, param: str, value: str):
        if param in VALID_PARAMS and value:
            self.params[param] = value
        return self

    # Add multiple params, receives a dict param: value
    def addParams(self, params: dict):
        for key, value in params.items():
            self.addParam(key, value)
        return self

    # Remove a param
    def removeParam(self, param: str):
        self.params.pop(param)
        return self

    # Remove multiple params, receives a list
    def removeParams(self, params: list):
        for param in params:
            self.params.pop(param)
        return self

    # Clears the actual params
    def clearParams(self):
        self.params = dict()
        return self

    # Get all params including the part
    def getParams(self):
        params = dict(self.params)
        params['part'] = self.part
        print(params)
        return params

    # Override the part param
    def overridePart(self, part: str):
        self.part = part
        return self

    # Execute the search
    def get(self):
        data = r.get(self.URL, params=self.getParams())
        return data

    # Makes a default search and return json
    def searchFor(self, q: str, maxResults=10, type='', extraOptions=dict()):
        params = {
            'q': q,
            'maxResults': maxResults,
            'type': type
        }
        self.addParams(params)
        self.addParams(extraOptions)
        return self.get().json()
