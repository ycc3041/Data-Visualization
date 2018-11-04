# Data-Visualization
This repository contains the implementation of several data visualization skills using different Python libraries.


## Prerequisites
* python 3.6
* matplotlib 2.2.2
* plotly 1.12.9
* seaborn 0.9.0
* bokeh 0.13.0
* networkx 1.11

## Project 1: Basic Visualization Techniques
#### *dataset: cars*

### || Bar chart
<img width="500" alt="task1_bar chart_europe" src="https://user-images.githubusercontent.com/44735519/47966802-aebf0980-e024-11e8-80b6-7777fd12c451.PNG">

### || Line chart
<img width="500" alt="task2_line chart" src="https://user-images.githubusercontent.com/44735519/47966806-b2529080-e024-11e8-9fd8-88013054e373.PNG">

### || Scatter plot
<img width="500" alt="task3_scatter plot" src="https://user-images.githubusercontent.com/44735519/47966808-b41c5400-e024-11e8-8579-5390146a007c.PNG">

### || Scatter plot matrix
![task4_scatter plot matrix](https://user-images.githubusercontent.com/44735519/47966845-d9a95d80-e024-11e8-8ebd-7aad70050ff1.png)


## Project 2: Visualization with Interaction
#### *dataset: countries*

### || Bubble chart
![p2-1](https://user-images.githubusercontent.com/44735519/47968862-87286b00-e03d-11e8-978b-88b97c86c79c.gif)

### || Bubble chart with widgets for users to choose each x,y ,radius and color
![p2-2](https://user-images.githubusercontent.com/44735519/47968863-88599800-e03d-11e8-8e72-bdd016346ff7.gif)

### || Bubble chart matrix with brushing, whereby the local selection of some data points in a visualization triggers the selection of the same data points in another visualization
![p2-3](https://user-images.githubusercontent.com/44735519/47968889-fdc56880-e03d-11e8-9764-9cb9d455c68f.gif)

### || Bubble chart matrix with hover, which trigger the display of all the attributes associated with a given data point.
![p2-4](https://user-images.githubusercontent.com/44735519/47968892-028a1c80-e03e-11e8-920a-f2163ac6d911.gif)


## Project 3: Networks Visualization
#### *dataset: 1997 US airlines*

### Networks graph which each node represents an airport and each edge represents the route
![p3-1](https://user-images.githubusercontent.com/44735519/47969027-d7083180-e03f-11e8-9872-c7224dd2722f.JPG)

### Networks graph which map the airports on real-world map 
![p3-2](https://user-images.githubusercontent.com/44735519/47969028-d7083180-e03f-11e8-8317-2bdfe3c73af3.gif)

### Networks graph with coloring and edge width to show the weights
![p3-3](https://user-images.githubusercontent.com/44735519/47969030-d7083180-e03f-11e8-891f-4492cdab8d6c.JPG)

### Networks with slider bars to filter the weights
![p3-5](https://user-images.githubusercontent.com/44735519/47969032-d7083180-e03f-11e8-8f84-07bf20c2e24b.gif)


## Instructions

For most of the python scripts, you can simply run the below command in the directory to show the visualization, except those using **bokeh**
```
python file_name.py
```

For those scripts using **bokeh**, run the below command instead to show the visualization
```
bokeh serve --show file_name.py
```
