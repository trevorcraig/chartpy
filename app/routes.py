from app import app
from flask import render_template
from chartpy import Scatter, Histogram

@app.route('/')
@app.route('/index')
def index():
    ScatChart=Scatter()
    ScatChart.AddDataSet(label="Example Dataset1", xdata=[1,2,3,4,5], ydata=[10,20,10,11,13], color="red")
    ScatChart.AddDataSet(label="Example Dataset2", xdata=[1,2,3,4,5], ydata=[15,25,15,16,8], color="blue")
    HistogramChart=Histogram()
    HistData=[174.191, 174.191, 175.089, 173.293, 173.293, 171.497, 172.395, 170.599, 170.599, 170.599, 171.497, 170.599, 172.395, 171.497, 170.599, 173.293, 173.293, 172.395, 173.293, 173.293, 174.191, 175.089, 175.089, 175.987, 175.987, 182.272, 185.863, 198.434, 219.983, 252.307, 289.121, 325.934, 356.463, 385.195, 407.643, 428.294, 445.354, 459.72, 474.984, 483.963]
    HistogramChart.AddDataSet(color="#c45850",xdata=HistData,label="Example Data")

    return render_template('example.html', ChartObj=ScatChart,ChartObj2=HistogramChart)
