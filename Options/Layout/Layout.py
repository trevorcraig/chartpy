# Libraries                                                   
import json
 
class Layout:
    def __init__(self):
        self.padding=self.Padding()
        
    def fromJson(self, JSONOBJ):
        JSONDATA=json.loads(JSONOBJ)
        Layout=JSONDATA["options"]["layout"]
        self.padding.fromJson(JSONOBJ)

    class Padding:
        def __init__(self):
            self.left=20
            self.right=20
            self.top=20
            self.bottom=20
            
        def fromJson(self, JSONOBJ):
            JSONDATA=json.loads(JSONOBJ)
            Padding=JSONDATA["options"]["layout"]["padding"]
            self.left=Padding["left"]
            self.right=Padding["right"]
            self.top=Padding["top"]
            self.bottom=Padding["bottom"]
