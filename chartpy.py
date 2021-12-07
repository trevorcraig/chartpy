# This project is to make plots that are compatible with charts.js
# Orginally started this project to only work the scatter plots
# Advantage of this code is using python for data edits and charts to plot

# Written by Trevor Craig
# Date: November 15, 2021

# Libraries                                                   
import json
from Data.Data import Data
from Options.Options import Options
from Data.Datasets.Datasets import Datasets
from Data.Datapoints.Datapoints import Datapoints
from Processors.Histogram import HistogramProcessor                                                              
            
class Scatter:
    def __init__(self,**kwargs):
        self.type="scatter"
        self.data=Data()
        self.options=Options()
        
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

    def AddDataSet(self,label,xdata,ydata,color):
        #This functions wants the x and y values as arrays!
        NewDataset=Datasets(pointBackgroundColor=color,label=label)

        for i in range(0,len(xdata)):
            datapoint=Datapoints()
            datapoint.x=xdata[i]
            datapoint.y=ydata[i]
            NewDataset.data.append(datapoint)
        self.data.datasets.append(NewDataset)

class Histogram:
    def __init__(self,**kwargs):
        self.type="bar"
        self.options=Options()
        # Some options are not avialble for histogram
        del self.options.scales.yAxes
        del self.options.scales.xAxes[0].type

        self.data=Data()
                
    def toJson(self):
        ReturnJson=json.dumps(self, default=lambda o: o.__dict__)
        return (ReturnJson)
    
    def fromJson(self, JSONOBJ):
        JSONDATA=json.loads(JSONOBJ)
        self.type=JSONDATA["type"]
        self.options.fromJson(JSONOBJ)
        self.data.fromJson(JSONOBJ)

    def AddDataSet(self,xdata,color,label):
        # Get the data we need for the dataset
        Histo=HistogramProcessor(xdata)
        [newlabels, newdata,newcolors]=Histo.ReturnData(color)
        NewDataset=Datasets(pointBackgroundColor=color,label=label)
        self.data.labels+=newlabels
        NewDataset.backgroundColor=newcolors
        NewDataset.data=newdata
        self.data.datasets.append(NewDataset)

class Line:
    def __init__(self,**kwargs):
        self.type="line"
        self.data=Data()
        self.options=Options()
        self.options.showLines="True"
        self.options.showLines="True"
        
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

    def AddDataSet(self,label,xdata,ydata,color):
        #This functions wants the x and y values as arrays!
        NewDataset=Datasets(pointBackgroundColor=color,label=label)

        for i in range(0,len(xdata)):
            datapoint=Datapoints()
            datapoint.x=xdata[i]
            datapoint.y=ydata[i]
            NewDataset.data.append(datapoint)
        self.data.datasets.append(NewDataset)