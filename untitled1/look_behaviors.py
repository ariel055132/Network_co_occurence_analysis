# -*- coding: utf-8 -*-

import csv

with open('1062_Shi_sequence_jumponly.csv') as f:
    reader = csv.reader(f)
    behaviors = []
    for row in reader:
        for i in range(1, len(row)):
            if row[i] not in behaviors:
                behaviors.append(row[i])
            if row[i]=='':
                break
print(behaviors)