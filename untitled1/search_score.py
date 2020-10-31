# -*- coding: utf-8 -*-

import csv
import pandas as pd


#分數檔名
score_filename = '1062_Shi_score'
#被篩選檔案名
filename = '1062_Shi_havescore_sequence'
#前or後幾趴
order = '_last'    #改reverse，> or <
part = 10


#讀分數檔，排序
score = pd.read_excel(score_filename + '.xlsx')
scores = []
for i in range(1,len(score)):
    scores.append((score['學期總成績'][i],score['Unnamed: 23'][i]))    
scores = sorted(scores, key=lambda s: s[1], reverse=False)

#分數篩選
scores_choice = []
num =len(scores)*part/100
if num%1 != 0:
    num = int(num)
else:
    num = int(num)-1
    
for i in range(len(scores)):
    if scores[i][1] > scores[num][1]:
        break
    scores_choice.append(scores[i][0])

#篩選出前幾%或後幾%的分數
with open (filename + '.csv', 'r', encoding='utf-8') as rf:
    with open(filename + order + str(part) + '%.csv', 'w', encoding='utf-8') as wf:
        wf.write(rf.readline())
        reader = csv.reader(rf)
        for row in reader:
            if row[0] in scores_choice:
                for i in range(len(row)):
                    wf.write(row[i])
                    if i == len(row)-1:
                        wf.write('\n')
                    else:
                        wf.write(',')