from .Datapoints.Datapoints import Datapoints
from .Datasets.Datasets import Datasets

class Data:
    def __init__(self,**kwargs):
        self.datasets=[]#Array of Datasets
        self.labels=[]
        
    def UpdateDataSet(self,DataSetNum,xdata,ydata):
        try:
            datapoint=Datapoints()
            datapoint.x=xdata
            datapoint.y=ydata
            self.datasets[DataSetNum].data.append(datapoint)
        except:
            print("Choose A valid Database!")
