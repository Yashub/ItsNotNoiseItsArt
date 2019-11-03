#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:00:34 2019

@author: shrikar.amirisetty
"""

import pandas
import numpy as np

names=['Danceability','Energy','Key','Loudness','Mode','Speechness','Acousticness','Instrumental','Liveness','Valence','Tempo','Time Signature','Genre']

songdb = pandas.read_csv('songdb.tsv',sep='\t',encoding = "ISO-8859-1",names=names)

csvdict = {}
for i in names:
    csvdict[i] = []

maingenres = {'r&b':0,'reggae':0,'country':0,'blues':0,'electronic':0,'classical':0,'jazz':0,'funk':0,'hiphop':0,'folk':0,'pop':0,'rock':0,'indie':0,'punk':0}

for i in range(len(songdb)):
    for j in maingenres:
        try:
            if i % 2 == 0 and songdb['Genre'][i] != '' and j in songdb['Genre'][i] and maingenres[j] != 700:
                for k in csvdict:
                    csvdict[k] += [songdb[k][i]]
                csvdict['Genre'].remove(songdb[k][i])
                csvdict['Genre'] += [j]
                maingenres[j] += 1
                break
        except:
            continue

csvdict['Tempo'] = [np.float64(i) for i in csvdict['Tempo']]
csvdict['Time Signature'] = [int(i) for i in csvdict['Time Signature']]
csvdict['Key'] = [int(i) for i in csvdict['Key']]
csvdict['Mode'] = [int(i) for i in csvdict['Mode']]

finalcsv = pandas.DataFrame(csvdict)

finalcsv.to_csv('finalcsv.csv',header=False,index=False)