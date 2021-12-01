from app import app
from flask import render_template
from chartpy import Scatter

@app.route('/')
@app.route('/index')
def index():
    ScatChart=Scatter()
    ScatChart.data.AddDataSet(label="Example Dataset1", xdata=[1,2,3,4,5], ydata=[10,20,10,11,13], color="red")
    ScatChart.data.AddDataSet(label="Example Dataset2", xdata=[1,2,3,4,5], ydata=[15,25,15,16,8], color="blue")
    return render_template('example.html', ChartObj=ScatChart)
