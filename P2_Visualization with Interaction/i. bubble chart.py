
# coding: utf-8

# # Programming Project 2: Interaction
# ● Due data: 9/20/2018

# In[2]:

import pandas as pd
from plotly.offline import plot

# In[3]:

df = pd.read_csv('factbook.csv')
df.head()


# In[4]:

df.columns


# ## Task 1: Bubble Chart
# - We saw in class a short clip of the famous TED Talk that Hans Rosling gave in 2006 in which he visualized global health statistics. For this first task, I am asking you to implement a basic bubble chart visualization, in other words a scatter plot in which individual data points are plotted as circles whose radius and color vary as a function of two variables (in addition to the two variables that control the (x,y) position of each circle). 
# - To demonstrate your bubble chart implementation, you will create following visualization: The x coordinate corresponds to 'GDP per capita', the y coordinate corresponds to 'Life expectancy at birth', the radius corresponds to 'Population', and the color corresponds to 'Birth rate'. Make sure to select scales, ranges, and color maps appropriately.

# In[5]:

import plotly.plotly as py
import plotly.graph_objs as go


# In[6]:

df[['Country', 'GDP per capita', 'Population','Birth rate']].head()


# In[7]:

df['Text'] = 'Country: ' + df['Country'] + '<br>' +     'GDP per capita: ' + df['GDP per capita'].astype(str) + '<br>'  +     'Population: ' + df['Population'].astype(str) + '<br>' +     'Birth rate: ' + df['Birth rate'].astype(str)


trace = go.Scatter(
    x = df['GDP per capita'],
    y = df['Life expectancy at birth'],
    mode = 'markers',
    text = df['Text'],
    marker=dict(
        size = df['Population'],
        symbol = 'circle',
        sizemode = 'area',
        # recommended formula:
        # sizeref = 2. * max(array of size values) / (desired maximum marker size ** 2)
        sizeref = 2. * max(df['Population']) / (150 ** 2),
        sizemin = 15,
        color = df['Birth rate'],
        showscale = True, 
        line = dict(
            width=2
        )
    )
)

data = [trace]

layout = go.Layout(
    title = 'Life Expectancy vs. GDP Per Capita',
    xaxis = dict(
        title = 'GDP Per Capita',
        gridcolor = 'rgb(255, 255, 255)',
        range = [2.5, 5],
        type = 'log',
        zerolinewidth = 1,
        ticklen = 5,
        gridwidth = 2,
    ),
    yaxis = dict(
        title = 'Life Expectancy',
        gridcolor = 'rgb(255, 255, 255)',
        range = [20, 90],
        zerolinewidth = 1,
        ticklen = 5,
        gridwidth = 2,
    ), 
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='1_Bubble Chart')
plot(fig)

