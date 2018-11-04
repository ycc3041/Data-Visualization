import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# transform raw data into dataframe

# node
node_data = pd.read_csv('nodes.csv', header=None)

node_split = node_data[0].str.split('"')

for i, col in enumerate(['id', 'name', 'xy']):
    if col == 'id':
        node_data[col] = node_split.apply(lambda x: int(x[i]))
    else:
        node_data[col] = node_split.apply(lambda x: x[i])

node_data['x'] = node_data['xy'].str.split().apply(lambda x: float(x[0]))
node_data['y'] = node_data['xy'].str.split().apply(lambda x: float(x[1]))

node_data.drop(0, axis=1, inplace=True)
node_data.drop('xy', axis=1, inplace=True)

# edge
edge_data = pd.read_csv('edges.csv', header=None)

edge_split = edge_data[0].str.split()

for i, col in enumerate(['from', 'to', 'frequency']):
        edge_data[col] = edge_split.apply(lambda x: float(x[i]))

edge_data.drop(0, axis=1, inplace=True)


# ********** 


# create graph
G = nx.Graph()

# node
for i in range(len(node_data)):
    G.add_node(node_data.iloc[i]['id'], 
               name=node_data.iloc[i]['name'], 
               pos=(node_data.iloc[i]['x'], node_data.iloc[i]['y']))

# edge
for i in range(len(edge_data)):
    G.add_edge(edge_data.iloc[i]['from'], 
               edge_data.iloc[i]['to'])

options = {
        'with_labels':1, # bool(True)
        # nodelist # list(G.nodes()); draw only specified nodes
        # edgelist # list(G.edges()); draw only specified edges
        'node_size':50, # scalar/array(300)
        'node_color':'#E74C3C', # color str/array of floats
        'alpha': 0.8,
        # cmap # colormap for mapping intensities of nodes
        'linewidths':0.5, # line witdth of symbol border
        'width': 0.5, # line width of edges
        'edge_color':'#AAAAA4', # color srt/array of floats
        # edge_cmap # colormap for mappig intensities of edges
        # style # edge line style(default:'solid')
        'labels':nx.get_node_attributes(G,'name'),
        'font_size':9, # (12)
        'font_color':'k', 
        # label # label for graph legend
        }


plt.figure(num=None, figsize=(40, 30), dpi=80, facecolor='w', edgecolor='k')

# without coordinates
## normal
#nx.draw(G, **options)

## network 
#nx.draw_networkx(G, **options)

## circular
#nx.draw_circular(G, **options)

## Kamada-Kawai force-directed layout
nx.draw_kamada_kawai(G, **options)

## spectral
#nx.draw_spectral(G, **options)  # super bad result

## spring
#nx.draw_spring(G, **options)

## shell
#nx.draw_shell(G, **options)

# with coordinates
## network drawing
#nx.draw(G, nx.get_node_attributes(G, 'pos'), **options)


plt.title('US Airlines 1997', fontsize = 30)
plt.show()