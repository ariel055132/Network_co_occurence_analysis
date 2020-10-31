# -*- coding: utf-8 -*-


import csv

with open('1062_Shi_sequence.csv', 'r') as rf:
    reader = csv.reader(rf)
    data = []
    max_sequence = 0
    last = ''
    for row in reader:
        sequence = []
        for i in range(len(row)):
            if row[i] =='':
                break
            if row[i] != last:
                sequence.append(row[i])
                last = row[i]
        data.append(sequence)
        if len(sequence) > max_sequence:
            max_sequence = len(sequence)

with open('1062_Shi_sequence_simple.csv', 'w') as wf:
    for sequence in data:
        for i in range(max_sequence):
            if i < len(sequence):
                wf.write(sequence[i])
            if i != max_sequence-1:
                wf.write(',')
            else:
                wf.write('\n')