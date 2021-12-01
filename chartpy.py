# This project is to make plots that are compatible with charts.js
# Orginally started this project to only work the scatter plots
# Advantage of this code is using python for data edits and charts to plot

# Written by Trevor Craig
# Date: November 15, 2021

# Libraries                                                   
import json                                                                  
            
class Scatter:
    def __init__(self,**kwargs):
        self.type="scatter"
        self.data=self.Data()
        self.options=self.Options()
        self.meta=self.Meta()
        
    def toJson(self):
        ReturnJson=json.dumps(self, default=lambda o: o.__dict__)
        return (ReturnJson)
    
    def fromJson(self, JSONOBJ):
        JSONDATA=json.loads(JSONOBJ)
        self.type=JSONDATA["type"]
        self.options.fromJson(JSONOBJ)
        self.data.fromJson(JSONOBJ)
        
    def toSession(self):
        ReturnJson=json.dumps(self, default=lambda o: o.__dict__)
        session["ChartObjJSOn"]=ReturnJson
                
    class Data:
        def __init__(self,**kwargs):
            self.datasets=[]#Array of Datasets
            
        def UpdateDataSet(self,DataSetNum,xdata,ydata):
            try:
                datapoint=self.Datapoints()
                datapoint.x=xdata
                datapoint.y=ydata
                self.datasets[DataSetNum].data.append(datapoint)
            except:
                print("Choose A valid Database!")
               
        def AddDataSet(self,label,xdata,ydata,color):
            #This functions wants the x and y values as arrays!
            NewDataset=self.Datasets()
            NewDataset.label=label
            NewDataset.pointBackgroundColor=color
            for i in range(0,len(xdata)):
                datapoint=self.Datapoints()
                datapoint.x=xdata[i]
                datapoint.y=ydata[i]
                NewDataset.data.append(datapoint)
            self.datasets.append(NewDataset)
            
            
        def fromJson(self, JSONOBJ):
            JSONDATA=json.loads(JSONOBJ)
            Datasets=JSONDATA["data"]["datasets"]
            count=0
            for dataset in Datasets:
                label=dataset["label"]
                color=dataset["pointBackgroundColor"]
                data=dataset["data"]
                xdata=[]
                ydata=[]
                for value in data:
                    xdata.append(value["x"])
                    ydata.append(value["y"])
                self.AddDataSet(label,xdata,ydata,color)
                #Set the other parmaters that might be common
                self.datasets[count].pointRadius=dataset["pointRadius"]
                self.datasets[count].pointHoverRadius=dataset["pointHoverRadius"]
                count=count+1
            
        class Datasets:
            def __init__(self, pointBackgroundColor="blue",pointRadius=4,pointHoverRadius=4, label="Label"):
                self.pointBackgroundColor=pointBackgroundColor
                self.pointRadius=pointRadius
                self.pointHoverRadius=pointHoverRadius
                self.label=label
                self.hidden=False
                self.data=[]#Array of datapoints
                
            class Meta:
                def __init__(self,well=None,channel=None):
                    self.well=well
                    self.channel=channel
            
        class Datapoints:
            def __init__(self):
                self.x=None
                self.y=None                    
            
    class Options:
        def __init__(self):
            self.responsive=True
            self.showLines=False
            self.layout=self.Layout()
            self.legend=self.Legend()
            self.scales=self.Scales()
            
        def fromJson(self, JSONOBJ):
            JSONDATA=json.loads(JSONOBJ)
            Options=JSONDATA["options"]
            self.responsive=Options["responsive"]
            self.showLines=Options["showLines"]
            self.layout.fromJson(JSONOBJ)
            self.legend.fromJson(JSONOBJ)
            self.scales.fromJson(JSONOBJ)
            
            print("We out here :D")
            
                    
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
                    
        
        class Legend:
            def __init__(self):
                self.display="false"
                
            def fromJson(self, JSONOBJ):
                JSONDATA=json.loads(JSONOBJ)
                Legend=JSONDATA["options"]["legend"]
                self.display=Legend["display"]
                
        class Scales:
            def __init__(self):
                self.xAxes=[self.XAxes()]
                self.yAxes=[self.YAxes()]
                
            def fromJson(self, JSONOBJ):
                JSONDATA=json.loads(JSONOBJ)
                Scales=JSONDATA["options"]["scales"]
                self.xAxes[0].fromJson(JSONOBJ)
                self.yAxes[0].fromJson(JSONOBJ)
                
            class XAxes:
                def __init__(self):
                    self.type='linear'
                    self.position='bottom'
                    
                def fromJson(self, JSONOBJ):
                    JSONDATA=json.loads(JSONOBJ)
                    xAxes=JSONDATA["options"]["scales"]["xAxes"][0]
                    self.type=xAxes["type"]
                    self.position=xAxes["position"]
                     
            class YAxes:
                def __init__(self):
                    self.type='linear'
                    self.position='left'
                    
                def fromJson(self, JSONOBJ):
                    JSONDATA=json.loads(JSONOBJ)
                    yAxes=JSONDATA["options"]["scales"]["yAxes"][0]
                    self.type=yAxes["type"]
                    self.position=yAxes["position"]

    class Meta:
        def __init__(self):
            self.wells=[]
            self.channels=[]
            self.testname="IDK"
            
