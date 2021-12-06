from .Legend.Legend import Legend
from .Scales.Scales import Scales
from .Layout.Layout import Layout
import json

class Options:
    def __init__(self):
        self.responsive=True
        self.showLines=False
        self.layout=Layout()
        self.legend=Legend()
        self.scales=Scales()
        
    def fromJson(self, JSONOBJ):
        JSONDATA=json.loads(JSONOBJ)
        Options=JSONDATA["options"]
        self.responsive=Options["responsive"]
        self.showLines=Options["showLines"]
        self.layout.fromJson(JSONOBJ)
        self.legend.fromJson(JSONOBJ)
        self.scales.fromJson(JSONOBJ)  