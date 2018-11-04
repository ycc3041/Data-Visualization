import pandas as pd
import networkx as nx
import matplotlib as mpl 
import matplotlib.pyplot as plt
from itertools import count
from plotly.graph_objs import *
from plotly.offline import plot
import plotly.offline as py
import numpy as np

# prepare for dataframe
# node
node_data = pd.read_csv('us_air_97.csv')
node_data.head()

# edge
edge_data = pd.read_csv('edges.csv', header=None)
edge_split = edge_data[0].str.split()

for i, col in enumerate(['from', 'to', 'frequency']):
        edge_data[col] = edge_split.apply(lambda x: float(x[i]))

edge_data.drop(0, axis=1, inplace=True)


#**************************************************#

# create graph
G = nx.Graph()


# add node
for i in range(len(node_data)):
    G.add_node(node_data.iloc[i]['ID'], 
               name=node_data.iloc[i]['old_name'],
               state=node_data.iloc[i]['state'],
               pos=(node_data.iloc[i]['lon'], node_data.iloc[i]['lat']))

# add edge
for i in range(len(edge_data)):
    G.add_edge(edge_data.iloc[i]['from'], 
               edge_data.iloc[i]['to'],
               frequency=edge_data.iloc[i]['frequency'])


#**************************************************#


# node color
groups = set(nx.get_node_attributes(G,'state').values())
mapping = dict(zip(sorted(groups), count()))
nodes = G.nodes()
node_color = [mapping[G.node[n]['state']] for n in nodes]

# node size
node_size = []
for i in range(len(node_data)):
    node_size.append(len(G[i+1]))

# edge width
edge_width = list(map(lambda x: x*5, edge_data['frequency'].values))

# edge color
edge_color = list(edge_data['frequency'].values)


#**************************************************#


# define positioning
pos = nx.kamada_kawai_layout(G)

# define scatter_nodes() and scatter_edges()
# these functions create plotly traces of the nodes and edges using the layout defined in pos
nodeID = G.node.keys()

def scatter_nodes(pos, labels=None, color='rgb(152, 0, 0)', size=node_size, opacity=1):
    trace = Scatter(x=[],
                    y=[],
                    mode='markers',
                    marker=Marker(
                            showscale=False,
                            colorscale='YlGnBu',
                            reversescale=True,
                            line=dict(width=0)))
    for nd in nodeID:
        trace['x'].append(pos[nd][0])
        trace['y'].append(pos[nd][1])
    attrib = dict(name='', text=labels, hoverinfo='text', opacity=opacity)
    trace=dict(trace, **attrib)
    trace['marker']['color']=node_color
    trace['marker']['size']=node_size
    return trace



def scatter_edges(G, pos, opacity=1):
    middle_node_trace = Scatter(
        x=[],
        y=[],
        mode='markers',
        hoverinfo='text',
        text=[],
        marker=Marker(opacity=0))
    
    trace = Scatter(x=[],
                    y=[],
                    mode='lines',
                    line=Line(color='#a3a3c2',
                              width=0.2
                            ),
                    hoverinfo='none'
                    )
                  
    i=0
    edge_f = nx.get_edge_attributes(G,'frequency')
    for edge in G.edges():
        trace['x'] += [pos[edge[0]][0],pos[edge[1]][0], None]
        trace['y'] += [pos[edge[0]][1],pos[edge[1]][1], None]  
        middle_node_trace['x'].append((pos[edge[0]][0]+pos[edge[1]][0])/2)
        middle_node_trace['y'].append((pos[edge[0]][1]+pos[edge[1]][1])/2)
        first = node_data[node_data['ID']==edge[0]]['old_name'].values[0]
        second = node_data[node_data['ID']==edge[1]]['old_name'].values[0]
        f = edge_f[(edge[0], edge[1])]
        middle_node_trace['text'].append('{} <-> {} <br>frequency: {}'.format(first, second, f))
        i += 1

    return trace, middle_node_trace


#**************************************************#


# node hover info
name = list(node_data['old_name'].values)
st = list(node_data['state'].values)
dg = node_size
fq = [0] * 332
for i in range(len(edge_data)):
    from_index = int(edge_data.iloc[i]['from'])
    to_index = int(edge_data.iloc[i]['to'])
    w = edge_data.iloc[i]['frequency']
    fq[from_index - 1] += w
    fq[to_index - 1] += w


node_label = []
for i in range(len(node_data)):
    node_label.append('airport: {}<br>state: {}<br>degree: {}<br>total frequency: {}'.format(name[i], st[i], dg[i], round(fq[i], 4)))


#**************************************************#

       
trace1, middle_trace = scatter_edges(G, pos)
trace2 = scatter_nodes(pos, labels=node_label)

width=1400
height=750
axis=dict(showline=False, # hide axis line, grid, ticklabels and  title
          zeroline=False,
          showgrid=False,
          showticklabels=False,
          title='' 
          )
layout=Layout(title= '',
    font= Font(),
    showlegend=False,
    autosize=False,
    width=width,
    height=height,
    xaxis=dict(
        title='US Air 1997',
        titlefont=dict(
        size=14,
        color='#fff'),
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False
    ),
    yaxis=YAxis(axis),
    margin=Margin(
        l=40,
        r=40,
        b=85,
        t=100,
        pad=0,
    ),
    hovermode='closest',
    paper_bgcolor='rgba(0,0,0,1)',
    plot_bgcolor='rgba(0,0,0,1)'
    )


#**************************************************#


data=Data([trace1, trace2, middle_trace])
fig = Figure(data=data, layout=layout)
plot(fig)

