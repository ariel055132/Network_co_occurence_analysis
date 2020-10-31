# -*- coding: utf-8 -*-

import csv
import numpy as np
import pandas as pd

#讀檔名
filename = '1062_Shi_sequence_poster_havescore'
professor_name = 'Shi'
#幾個編碼
gram = 2
tail = gram-1

#建立lable順序
with open(professor_name + '/sequence/' + filename + '.csv') as f:
    reader = csv.reader(f)
    behaviors = {}
    dict_num = 0
    for row in reader:
        for i in range(1,len(row)-tail):
            if row[i+tail] == '':
                break
            
            label = row[i]
            for j in range(1,gram):
                label += row[i+j]
            
            if label not in behaviors:
                behaviors[label] = dict_num
                dict_num += 1

#建立矩陣           
with open(professor_name + '/sequence/' + filename + '.csv') as f:
    reader = csv.reader(f)
    matrix = np.zeros((len(behaviors), len(behaviors)))
    for row in reader:
        for i in range(2,len(row)-tail):
            if row[i+tail] == '':
                break

            label1 = row[i-1]
            label2 = row[i]
            for j in range(1,gram):
                label1 += row[i-1+j]
                label2 += row[i+j]
                
            matrix[behaviors[label1]][behaviors[label2]] += 1
            # comment the following line for building directed graph
            #matrix[behaviors[label2]][behaviors[label1]] += 1

#改檔名
filename = filename.replace('sequence', 'matrix')

#匯出矩陣
matrix = pd.DataFrame(matrix, index=list(behaviors.keys()), columns=list(behaviors.keys()))
#matrix.to_csv(professor_name + '/'+ str(gram) +'gram/' + filename + '.csv')
matrix.to_csv(professor_name + '/'+ str(gram) +'gram/' + filename + '_directed' + '.csv')