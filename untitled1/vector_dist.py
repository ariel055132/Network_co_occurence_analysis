import numpy as np
from sklearn.cluster import KMeans

# 歐幾里得距離...
# K-Means with 歐幾里得距離 --> wrong

# 歐幾里得距離
def eu_dist(x, y):
    x = np.array(x)
    y = np.array(y)
    return np.sqrt(np.sum((x-y)**2))

filename = '1062_Shi_matrix_havescore_directed'
professor_name = 'Shi'
gram = 2

file = np.loadtxt(professor_name + '/' + str(gram) + 'gram/' + filename + '.csv', dtype=np.str, delimiter=',')
data = file[1:, 1:].astype(np.float)
sequence_name_list_Shi = ["sequenceO", "sequenceN", "sequenceP", "sequenceD", "sequenceA", "sequenceF", "sequenceB", "sequenceG", "sequenceC", "sequenceJ", "sequenceS", "sequenceE", "sequenceH"]
sequence_name_list_Young = ["sequenceO", "sequenceN", "sequenceA", "sequenceP", "sequenceF", "sequenceC", "sequenceD", "sequenceH", "sequenceB", "sequenceE", "sequenceJ", "sequenceG", "sequenceL", "sequenceS"]
distance = []

'''
for i in range(len(sequence_name_list)):
    temp_list = data[i][0:].tolist()
    sequence_name_list[i] = temp_list
    #print(sequence_name_list[i])
'''

for i in range(0, 151):
    temp_list = data[i][0:].tolist()
    distance.append(temp_list)

clf = KMeans(n_clusters=3)
clf.fit(distance)
print(clf.labels_)
