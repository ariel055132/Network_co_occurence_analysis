import numpy as np
from numpy import dot
from numpy.linalg import norm
from sklearn import cluster

def cosine_measure(vector1, vector2):
    cos_sim = dot(vector1, vector2)/(norm(vector1)*norm(vector2))
    return cos_sim

filename = '1062_Shi_matrix_poster_havescore_directed'
professor_name = 'Shi'
gram = 1

file = np.loadtxt(professor_name + '/' + str(gram) + 'gram/' + filename + '.csv', dtype=np.str, delimiter=',')
data = file[2:, 2:].astype(np.float)
sequence_name_list = ["sequenceO", "sequenceN", "sequenceP", "sequenceD", "sequenceA", "sequenceF", "sequenceB", "sequenceG", "sequenceC", "sequenceJ", "sequenceS", "sequenceE", "sequenceH"]
cosine_similarity_data = []

# save the data from csv file to sequence_name_list one by one, starts with "sequenceO", ends with "sequenceH"
for i in range(len(sequence_name_list)):
    temp_list = data[i][0:].tolist()
    sequence_name_list[i] = temp_list

# this for loop is bad, should be rewrite, sry...
for i in range(len(sequence_name_list)):
    # ON-OH
    if i == 0:
        for j in range(1, 13):
            cosine_similarity_data.append(cosine_measure(sequence_name_list[i], sequence_name_list[j]))
    # NP-NH
    elif i == 1:
        for j in range(2, 13):
            cosine_similarity_data.append(cosine_measure(sequence_name_list[i], sequence_name_list[j]))
    # PD-PH
    elif i == 2:
        for j in range(3, 13):
            cosine_similarity_data.append(cosine_measure(sequence_name_list[i], sequence_name_list[j]))
    # DA-DH
    elif i == 3:
        for j in range(4, 13):
            cosine_similarity_data.append(cosine_measure(sequence_name_list[i], sequence_name_list[j]))
    # AF-AH
    elif i == 4:
        for j in range(5, 13):
            cosine_similarity_data.append(cosine_measure(sequence_name_list[i], sequence_name_list[j]))
    # FB-FH
    elif i == 5:
        for j in range(6, 13):
            cosine_similarity_data.append(cosine_measure(sequence_name_list[i], sequence_name_list[j]))
    # BG-BH
    elif i == 6:
        for j in range(7, 13):
            cosine_similarity_data.append(cosine_measure(sequence_name_list[i], sequence_name_list[j]))
    # GC-GH
    elif i == 7:
        for j in range(8, 13):
            cosine_similarity_data.append(cosine_measure(sequence_name_list[i], sequence_name_list[j]))
    # CJ-CH
    elif i == 8:
        for j in range(9, 13):
            cosine_similarity_data.append(cosine_measure(sequence_name_list[i], sequence_name_list[j]))
    # JS-JH
    elif i == 9:
        for j in range(10, 13):
            cosine_similarity_data.append(cosine_measure(sequence_name_list[i], sequence_name_list[j]))
    # SE-SH
    elif i == 10:
        for j in range(11, 13):
            cosine_similarity_data.append(cosine_measure(sequence_name_list[i], sequence_name_list[j]))
    # EH
    elif i == 11:
        for j in range(12, 13):
            cosine_similarity_data.append(cosine_measure(sequence_name_list[i], sequence_name_list[j]))

for i in range(len(cosine_similarity_data)):
    print(cosine_similarity_data[i])

# get the size of dataset
dataset_size = len(cosine_similarity_data)
# convert to 2-D array
cosine_similarity_data = np.array(cosine_similarity_data).reshape(1, -1)
# scikit-learn read each list as a sample, error appears when the following code is not write
# https://blog.csdn.net/CY_TEC/article/details/77931820
# convert each element to list --> 3-D array
cosine_similarity_data = [[i] for i in cosine_similarity_data]
# convert 3-D array to 2-d ARRAY for sk-learn to fit and print the results
cosine_similarity_data = np.array(cosine_similarity_data).reshape(dataset_size, -1)
clf = cluster.KMeans(n_clusters=4).fit(cosine_similarity_data)
cluster_labels = clf.labels_
# Print the clustering results
print("cluster results: ")
print(cluster_labels)
print("-------")

