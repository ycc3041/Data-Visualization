# Data-Visualization
This repository contains the implementation of several data visualization skills using different Python libraries.


## Prerequisites
* python 3.6
* matplotlib 2.2.2
* plotly 1.12.9
* seaborn 0.9.0
* bokeh 0.13.0
* networkx 1.11


## Project 1: Basic Visualization Techniques with Car Dataset
[Code Here](https://github.com/ycc3041/Data-Visualization/blob/master/P1_Basic%20Visualization%20Techniques/Basic%20Visualization%20Techniques.ipynb)

### || Bar chart
<img width="500" alt="task1_bar chart_europe" src="https://user-images.githubusercontent.com/44735519/47966802-aebf0980-e024-11e8-80b6-7777fd12c451.PNG">

### || Line chart
<img width="500" alt="task2_line chart" src="https://user-images.githubusercontent.com/44735519/47966806-b2529080-e024-11e8-9fd8-88013054e373.PNG">

### || Scatter plot
<img width="500" alt="task3_scatter plot" src="https://user-images.githubusercontent.com/44735519/47966808-b41c5400-e024-11e8-8579-5390146a007c.PNG">

### || Scatter plot matrix
![task4_scatter plot matrix](https://user-images.githubusercontent.com/44735519/47966845-d9a95d80-e024-11e8-8ebd-7aad70050ff1.png)


## Project 2: Visualization with Interaction with Countries Dataset

### || Bubble chart
[Code Here](https://github.com/ycc3041/Data-Visualization/blob/master/P2_Visualization%20with%20Interaction/i.%20bubble%20chart.py)
![p2-1](https://user-images.githubusercontent.com/44735519/47970089-bdbab180-e04e-11e8-991e-028cb81e9309.gif)

### || Bubble chart with widgets
#### Users can choose each x,y ,radius and color
[Code Here](https://github.com/ycc3041/Data-Visualization/blob/master/P2_Visualization%20with%20Interaction/ii.%20widgets.py)
![p2-2](https://user-images.githubusercontent.com/44735519/47968863-88599800-e03d-11e8-8e72-bdd016346ff7.gif)


### || Bubble chart matrix with brushing
#### The local selection of some data points in a visualization triggers the selection of the same data points in another visualization
[Code Here](https://github.com/ycc3041/Data-Visualization/blob/master/P2_Visualization%20with%20Interaction/iii.%20brushing.py)
![p2-3](https://user-images.githubusercontent.com/44735519/47968889-fdc56880-e03d-11e8-9764-9cb9d455c68f.gif)


### || Bubble chart matrix with hover
#### The hover over points trigger the display of all the attributes associated with a given data point
[Code Here](https://github.com/ycc3041/Data-Visualization/blob/master/P2_Visualization%20with%20Interaction/iv.%20hover.py)
![p2-4](https://user-images.githubusercontent.com/44735519/47968892-028a1c80-e03e-11e8-920a-f2163ac6d911.gif)


## Project 3: Networks Visualization with 1997 US Airlines Dataset

### || Networks graph 
#### Each node represents an airport and each edge represents a route
[Code Here](https://github.com/ycc3041/Data-Visualization/blob/master/P3_Networks%20Visualization/i.%20basic%20networks%20visualization.py)
![p3-1](https://user-images.githubusercontent.com/44735519/47970126-315cbe80-e04f-11e8-8188-d8d244d9a06e.JPG)

### || Geospatial networks visualization
#### Each airport is mapped on real-world map based on their latitude and longitude
[Code Here](https://github.com/ycc3041/Data-Visualization/blob/master/P3_Networks%20Visualization/ii.%20geospatial%20visualization.py)
![p3-2](https://user-images.githubusercontent.com/44735519/47970127-315cbe80-e04f-11e8-8ac5-3549296cd600.gif)

### || Weighted networks graph
#### Coloring and edge width show the weight/frequency/importance of nodes and edges
[Code Here](https://github.com/ycc3041/Data-Visualization/blob/master/P3_Networks%20Visualization/iii.%20complex%20networks%20visualization.py)
![p3-3](https://user-images.githubusercontent.com/44735519/47970128-315cbe80-e04f-11e8-98db-327170ec7b26.JPG)

### || Networks with slider bars 
#### Slider bars allow filtering different weights of nodes or edges to be shown 
[Code Here](https://github.com/ycc3041/Data-Visualization/blob/master/P3_Networks%20Visualization/v.%20networks%20with%20filtering.py)
![p3-5](https://user-images.githubusercontent.com/44735519/47970136-40dc0780-e04f-11e8-8dca-9a8939ff632b.gif)


## Instructions

For most of the python scripts, you can simply run the below command in the directory to show the visualization, except those using **bokeh**
```
python file_name.py
```

For those scripts using **bokeh**, run the below command instead to show the visualization
```
bokeh serve --show file_name.py
```
