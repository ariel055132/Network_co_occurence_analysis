# -*- coding: utf-8 -*-

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#檔名
filename = '1062_Shi_matrix_poster_havescore_directed'
professor_name = 'Shi'
gram = 3

file = np.loadtxt(professor_name + '/' + str(gram) + 'gram/' + filename + '.csv', dtype=np.str, delimiter=',')
data = file[1:,1:].astype(np.float)
labels = file[1:,0]
count = np.zeros((1,len(labels)))
for i in range(len(labels)):
    for j in range(len(labels)):
        count[0][i] = count[0][i] + data[i][j]


'''
for i in range(len(labels)):
    clf = KMeans(n_clusters=3)
    clf.fit(count)
    plt.scatter(count[0][i], c=clf.labels_)
plt.show()
'''

'''
plt.scatter(data[:, :], data[:, :])
clf = KMeans(n_clusters=4)
clf.fit(data)
clf.labels_
#plt.scatter(data[:, 0], data[:, 1], c=clf.labels_)
plt.show()
'''