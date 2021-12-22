# chartpy
chartpy lets you manage charts in your Flask application.

This is compatible with Chart.js


Getting Started
===============
Install flask with command below or with requirments folder:

    pip install flask

Clone this project and add it to your directory. 

Using it
========

A simple Line Chart example.

# 1. Create the HTML file
```
<canvas id="myChart"></canvas>
{% block javascript %}
	<script type="text/javascript">
		data = {{ChartObj.toJson()|safe}};
		window.myLineChart =new Chart(document.getElementById("myChart"),data);
	</script>
{% endblock %}
```
    
# 2. Create the chart in python

```
from app import app
from flask import render_template
from chartpy import Scatter, Histogram, Line

@app.route('/')
@app.route('/index')
def index():
	LineChart=Line()
	LineChart.AddDataSet(label="Example Dataset1", xdata=[1,2,3,4,5], ydata=[1,3,2,5,4], color="red")
	LineChart.AddDataSet(label="Example Dataset2", xdata=[1,2,3,4,5], ydata=[2,4,3,6,5], color="blue")
	return render_template('example.html', ChartObj=LineChart)
```

# 3. Get a Chart.js Line Chart
![plot](./docs/linechart.png)


 
I find this much more convient than using the javascript.
To run it all you need to do is install and run 
"flask run"

An example of how to do it is attached with the app.
## Curent Supported Graphs
# scatter
# histogram
# line



# FUTRUE PLANS
I plan on adding more chart options. Feel free to add or request your own favorite charts.

Check out https://github.com/chartjs/Chart.js and support that project!
