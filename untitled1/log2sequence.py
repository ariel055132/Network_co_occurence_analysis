# -*- coding: utf-8 -*-

import csv

user_behavior = 10
user_id = 14
data = {}
max_sequence = 0
with open('1062_Shi_log.csv', 'r', encoding='utf-8') as rf:
    reader = csv.reader(rf)
    temp = {}
    first = True
    for row in reader:
        if first:
            first = False
            continue
        user = row[user_id]
        behavior = row[user_behavior]
        if user not in temp:
            temp[user] = []
        if behavior == 'OPEN' and 'OPEN' in temp[user]:
            if user not in data:
                data[user] = []
            data[user].append(temp[user])
            if len(temp[user]) > max_sequence:
                max_sequence = len(temp[user])
            temp[user] = ['OPEN']
        else:
            temp[user].append(behavior)
    for user in temp:
        if user not in data:
            data[user] = []
        data[user].append(temp[user])
        if len(temp[user]) > max_sequence:
                max_sequence = len(temp[user])
    temp.clear()

with open('1062_Shi_sequence.csv', 'w') as wf:
    wf.write('userid,sequence,')
    for i in range(max_sequence-2):
        wf.write(',')
    wf.write('\n')
    for key in data:
        for sequence in data[key]:
            wf.write(key + ',')
            for i in range(max_sequence):
                if i < len(sequence):
                    wf.write(sequence[i])
                if i != max_sequence-1:
                    wf.write(',')
                else:
                    wf.write('\n')