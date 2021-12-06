from .XAxes.XAxes import XAxes
from .YAxes.YAxes import YAxes

import json

class Scales:
    def __init__(self):
        self.xAxes=[XAxes()]
        self.yAxes=[YAxes()]
        
    def fromJson(self, JSONOBJ):
        JSONDATA=json.loads(JSONOBJ)
        Scales=JSONDATA["options"]["scales"]
        self.xAxes[0].fromJson(JSONOBJ)
        self.yAxes[0].fromJson(JSONOBJ)