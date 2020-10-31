# -*- coding: utf-8 -*-

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#檔名
filename = '1062_Shi_matrix_poster_havescore_directed'
professor_name = 'Shi'
gram = 3
#共現次數篩選
filter_num = 50

file = np.loadtxt(professor_name + '/' + str(gram) + 'gram/' + filename + '.csv', dtype=np.str, delimiter=',')
data = file[1:, 1:].astype(np.float)
labels = file[1:, 0]
count = np.zeros((1, len(labels)))
for i in range(len(labels)):
    for j in range(len(labels)):
        count[0][i] = count[0][i] + data[i][j]

#建立圖
G = nx.DiGraph()

#設定node和edge
nodes = []
for i in range(len(labels)):
    for j in range(i+1, len(labels)):
        if data[i][j] < filter_num:
            continue
        if labels[i] not in nodes:
            G.add_node(labels[i], size=10+count[0][i]/10)
        if labels[j] not in nodes:
            G.add_node(labels[j], size=10+count[0][j]/10)
        G.add_edge(labels[i], labels[j], weight=data[i][j]/1000)

# positions for all nodes
pos = nx.spring_layout(G)

# nodes
for i in G:
    nx.draw_networkx_nodes(G, pos, nodelist=[i], node_size=G.nodes[i]['size'], alpha=0.5)
    
# edges
for i in G.edges():
    nx.draw_networkx_edges(G, pos, edgelist=[i], width=G.edges[i]['weight'], arrows=True)

# Calculate Betweenness Centrality
# https://medium.com/@pasdan/centrality-metrics-via-networkx-python-5c9ce52909c0
betweeness_centrality = nx.betweenness_centrality(G)
print(betweeness_centrality)

#改檔名
filename = filename.replace('matrix', 'network')
   
# labels
nx.draw_networkx_labels(G, pos, font_size=5, font_family='sans-serif', font_color='g')
plt.axis('off')
plt.title(filename + '_' + str(filter_num))
plt.show()

# save the picture and put it into folder picture (optional)
# ValueError: Format 'jpg' is not supported (supported formats: eps, pdf, pgf, png, ps, raw, rgba, svg, svgz)
#plt.savefig('picture/' + str(gram) + 'gram/' + filename + '.png', dpi=100)
#plt.savefig('picture/' + str(gram) + 'gram/' + "test75" + '.pdf', dpi=1000)
