import json

class XAxes:
    def __init__(self):
        self.type='linear'
        self.position='bottom'
        self.barPercentage=1.0
        self.categoryPercentage=1.0
        
    def fromJson(self, JSONOBJ):
        JSONDATA=json.loads(JSONOBJ)
        xAxes=JSONDATA["options"]["scales"]["xAxes"][0]
        self.type=xAxes["type"]
        self.position=xAxes["position"]
