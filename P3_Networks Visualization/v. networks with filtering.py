import pandas as pd
import networkx as nx
import matplotlib as mpl 
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.widgets import Slider

# prepare for dataframe
# node
node_data = pd.read_csv('us_air_97.csv')

# edge
edge_data = pd.read_csv('edges.csv', header=None)
edge_split = edge_data[0].str.split()

for i, col in enumerate(['from', 'to', 'frequency']):
        edge_data[col] = edge_split.apply(lambda x: float(x[i]))

edge_data.drop(0, axis=1, inplace=True)

fq = [0] * 332
for i in range(len(edge_data)):
    from_index = int(edge_data.iloc[i]['from'])
    to_index = int(edge_data.iloc[i]['to'])
    w = edge_data.iloc[i]['frequency']
    fq[from_index - 1] += w
    fq[to_index - 1] += w

node_data['degree'] = fq

groups = set(node_data['state'].values)
mapping = dict(zip(sorted(groups), count()))
node_data['stateNo'] = [mapping[node_data.iloc[n]['state']] for n in range(len(node_data))]


# node_data.head()
# edge_data.head()


#**************************************************#

def create_plot(min_degree=0, min_freq=0):
    # fig = plt.figure(figsize=(20, 20))
    G = nx.Graph()
    selected_nodes = node_data[node_data['degree']>=som1.val]
    
    node_id = set(selected_nodes['ID'].values)
    selected_edges = edge_data[(edge_data['frequency']>=som2.val) & (edge_data['from'].isin(node_id)) & (edge_data['to'].isin(node_id))]

    # node
    for i in range(len(selected_nodes)):
        G.add_node(selected_nodes.iloc[i]['ID'], 
                   name=selected_nodes.iloc[i]['old_name'],
                   state=selected_nodes.iloc[i]['state'],
                   pos=(selected_nodes.iloc[i]['lon'], selected_nodes.iloc[i]['lat']))
    
    # edge
    for i in range(len(selected_edges)):
        G.add_edge(selected_edges.iloc[i]['from'], 
                   selected_edges.iloc[i]['to'])

    # node color
    colors = list(selected_nodes['stateNo'].values)
    
    # node size
    node_size = list(map(lambda x: x*150, selected_nodes['degree'].values))
#    node_size = []
#    for i in range(len(selected_nodes)):
#        node_size.append(len(G[i+1])*15)
    
    # edge width
    edge_width = list(map(lambda x: x*10, selected_edges['frequency'].values))
    
    # edge color
    edge_color = selected_edges['frequency']

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
            'font_size':6, # (12)
            'font_color':'k', 
            'label': 'test123' # label for graph legend
            }
    ax.clear()
    nx.draw_kamada_kawai(G, ax=ax, **options)


    
fig, ax = plt.subplots(1, 1, figsize=(30, 40))
plt.subplots_adjust(bottom=0.2, left=0.3)
# fig = plt.figure(figsize=(20, 20))


axcolor = 'lightgrey'
om1= plt.axes([0.25, 0.1, 0.6, 0.02], facecolor=axcolor)
om2 = plt.axes([0.25, 0.05, 0.6, 0.02], facecolor=axcolor)
som1 = Slider(om1, 'Minimum node weight', 0, 10, valinit=1.5)
som2 = Slider(om2, 'Minimum edge frequency', 0, 0.4, valinit=0.03)

som1.on_changed(create_plot)
som2.on_changed(create_plot)

# initialization
create_plot()

# plt.title('US Air 1997', fontsize = 30)
plt.show()


