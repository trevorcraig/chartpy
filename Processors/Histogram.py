import math
class HistogramProcessor:
    def __init__(self,values):
        self.values=values.copy()
        self.values.sort()
        self.FindBins()
        self.FindSpacing()
        self.MakeBins()
        self.PlaceIntoBins()

    def FindBins(self):
        self.NumberofBins=int(math.log(len(self.values),(2))+1)

    def FindSpacing(self):
        self.Spacing=(max(self.values)-min(self.values))/self.NumberofBins
    
    def MakeBins(self):
        Bins=[]
        FirstValue=min(self.values)
        for i in range(0,self.NumberofBins):
            Binny=self.Bin(FirstValue,FirstValue+self.Spacing)
            Bins.append(Binny)
            FirstValue=FirstValue+self.Spacing

        self.Bins=Bins

    # slightly slopy way of making bins
    def PlaceIntoBins(self):
        BinNumber=0
        for value in self.values:
            while (BinNumber<self.NumberofBins):
                if (value >= self.Bins[BinNumber].Low) and (value <= self.Bins[BinNumber].High):
                    self.Bins[BinNumber].NumberofValues=self.Bins[BinNumber].NumberofValues+1
                    break
                BinNumber=BinNumber+1

    def ReturnData(self,color):
        Labels=[]
        Values=[]
        Colors=[]
        for bi in self.Bins:
            Labels.append(bi.Label)
            Values.append(bi.NumberofValues)
            Colors.append(color)
        return([Labels,Values,Colors])
    
    class Bin:
        def __init__(self,low,high):
            self.Low=low
            self.High=high
            self.NumberofValues=0
            #self.Label=str(low)+"-"+str(high)
            self.Label=f'{low:.2f} to {high:.2f}'
