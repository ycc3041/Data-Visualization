import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.basemap import Basemap as Basemap


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

# **********

G = nx.Graph()

plt.figure(figsize=(20, 20))

m = Basemap(projection='merc',
            llcrnrlon=-180,
            llcrnrlat=10,
            urcrnrlon=-50, 
            urcrnrlat=70, 
            lat_ts=0, 
            resolution='l',
            suppress_ticks=True)

# node
for i in range(len(node_data)):
    G.add_node(node_data.iloc[i]['ID'], 
               name=node_data.iloc[i]['old_name'],
               state=node_data.iloc[i]['state'],
               pos=(node_data.iloc[i]['lon'], node_data.iloc[i]['lat']))

# edge
for i in range(len(edge_data)):
    G.add_edge(edge_data.iloc[i]['from'], 
               edge_data.iloc[i]['to'])

# position
m_x, m_y = m(node_data['lon'].values, node_data['lat'].values)
pos = {}
for i, elem in enumerate(node_data['ID']):
    pos[elem] = (m_x[i], m_y[i])

# coloring
from itertools import count
groups = set(nx.get_node_attributes(G,'state').values())
mapping = dict(zip(sorted(groups), count()))
nodes = G.nodes()
colors = [mapping[G.node[n]['state']] for n in nodes]

options = {
        'with_labels':1, # bool(True)
        # nodelist # list(G.nodes()); draw only specified nodes
        # edgelist # list(G.edges()); draw only specified edges
        'node_size':40, # scalar/array(300)
        'node_color':colors, # color str/array of floats
        'alpha': 0.8,
        'cmap':plt.cm.tab10, # colormap for mapping intensities of nodes
        'linewidths':0.5, # line witdth of symbol border
        'width': 0.5, # line width of edges
        'edge_color':'#AAAAA4', # color srt/array of floats
        # edge_cmap # colormap for mappig intensities of edges
        # style # edge line style(default:'solid')
        'labels':nx.get_node_attributes(G,'name'),
        'font_size':8, # (12)
        'font_color':'k', 
        # label # label for graph legend
        }

nx.draw(G, pos, **options)
m.drawcountries(linewidth = 0.5)
m.drawstates(linewidth = 1)
m.drawcoastlines(linewidth = 1)

plt.show()

