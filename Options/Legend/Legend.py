import json

class Legend:
    def __init__(self):
        self.display="false"
        
    def fromJson(self, JSONOBJ):
        JSONDATA=json.loads(JSONOBJ)
        Legend=JSONDATA["options"]["legend"]
        self.display=Legend["display"]
