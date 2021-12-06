import json

class YAxes:
    def __init__(self):
        self.type='linear'
        self.position='left'
        
    def fromJson(self, JSONOBJ):
        JSONDATA=json.loads(JSONOBJ)
        yAxes=JSONDATA["options"]["scales"]["yAxes"][0]
        self.type=yAxes["type"]
        self.position=yAxes["position"]
