import pandas as pd
from plotly.offline import plot
import plotly.plotly as py
import plotly.graph_objs as go


df = pd.read_csv('factbook.csv')
df.head()


df[['Country', 'GDP per capita', 'Population','Birth rate']].head()


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

