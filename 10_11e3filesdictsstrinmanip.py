#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:07:40 2019

@author: ACAN
"""

import string
string.punctuation

counts={}

fhand = open("prideandprejudice.txt")
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

countlist = []
for key, value in counts.items():
    tup = value,key
    countlist.append(tup)

print(countlist[:30])
countlist.sort(reverse=True)
print(countlist[:30])
#done for words not letters.