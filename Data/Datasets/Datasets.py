class Datasets:
    def __init__(self, pointBackgroundColor="blue",pointRadius=4,pointHoverRadius=4, label="Label"):
        self.pointBackgroundColor=pointBackgroundColor
        self.pointRadius=pointRadius
        self.pointHoverRadius=pointHoverRadius
        self.backgroundColor=pointBackgroundColor
        self.borderColor=pointBackgroundColor
        self.label=label
        self.hidden=False
        self.fill=False
        self.data=[]#Array of datapoints
