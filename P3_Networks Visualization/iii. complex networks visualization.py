import pandas as pd
import networkx as nx
import matplotlib as mpl 
import matplotlib.pyplot as plt
from matplotlib import gridspec
from itertools import count


#**************************************************#
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
# create plot


fig, ax = plt.subplots(3, 1, figsize=(30, 30))
gs = gridspec.GridSpec(4, 1, height_ratios=[30, 1, 0.5, 0.5])

#**************************************************#
# create network


G = nx.Graph()

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

# node color
groups = set(nx.get_node_attributes(G,'state').values())
mapping = dict(zip(sorted(groups), count()))
nodes = G.nodes()
colors = [mapping[G.node[n]['state']] for n in nodes]

# node size
node_size = []
for i in range(len(node_data)):
    node_size.append(len(G[i+1])*15)

# edge width
edge_width = list(map(lambda x: x*10, edge_data['frequency'].values))

# edge color
edge_color = edge_data['frequency']

options = {
        'with_labels':1, # bool(True)
        # nodelist # list(G.nodes()); draw only specified nodes
        # edgelist # list(G.edges()); draw only specified edges
        'node_size':node_size, # scalar/array(300)
        'node_color':colors, # color str/array of floats
        'alpha': 0.7,
        'cmap':plt.cm.tab10, # colormap for mapping intensities of nodes
        'linewidths':0.5, # line witdth of symbol border
        'width':edge_width, # line width of edges
        'edge_color':edge_color, # color srt/array of floats
        'edge_cmap':plt.cm.Greys, # colormap for mappig intensities of edges
        # style # edge line style(default:'solid')
        'labels':nx.get_node_attributes(G,'name'),
        'font_size':7, # (12)
        'font_color':'k', 
        'label': 'test123' # label for graph legend
        }

ax0 = plt.subplot(gs[0])
nx.draw_kamada_kawai(G, **options)
ax0.set_title('US Air 1997', fontsize = 30)


#**************************************************#
# create two legends


# ax1= plt.axes([0.15, 0.1, 0.6, 0.02])

# colorbar legend: edge frequeny
vmin = min(edge_color)
vmax = max(edge_color)
sm = plt.cm.ScalarMappable(cmap=plt.cm.Greys, norm=mpl.colors.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
l1 = plt.subplot(gs[1])
c = plt.colorbar(sm, cax=l1, shrink = 0.1, orientation='horizontal')
c.ax.set_title('Frequency')

# size legend: node degree
l1 = plt.scatter([],[], s=50, edgecolors='none')
l2 = plt.scatter([],[], s=500, edgecolors='none')
l3 = plt.scatter([],[], s=750, edgecolors='none')
l4 = plt.scatter([],[], s=1000, edgecolors='none')

labels = ['5', '50', '75', '100']

ax3 = plt.subplot(gs[3])
#ax2 = plt.axes([0.05, 0.05, 0.4, 0.02])
plt.axis('off')
leg = plt.legend([l1, l2, l3, l4], 
                 labels, 
                 ncol=4, 
                 frameon=True, 
                 fontsize=10,
                 handlelength=2, 
                 loc = 10, 
                 borderpad = 1.8,
                 handletextpad=1, 
                 title='Node Degree', 
                 scatterpoints = 1)

#**************************************************#

plt.show()


