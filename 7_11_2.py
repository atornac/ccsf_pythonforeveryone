#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:58:25 2019

@author: acan
"""

#7_11_2
filename = input("Enter file name:")

spam_confidence = []
spam_confidence_float = []

"""
fhand2 = open(filename)

for line in fhand2:
    if line.find("X-DSPAM-Confidence") == -1: #means did not find
        continue
    else:
        index = line.find(":")+1
        spam_confidence.append(line[index:-1])

for x in spam_confidence:
    spam_confidence_float.append(float(x))
    
print(spam_confidence)
print(spam_confidence_float)

average_scf = sum(spam_confidence_float)/len(spam_confidence_float)
print (average_scf)
"""
#below accounts for bad file name choice

try:
    fhand2 = open(filename)
    for line in fhand2:
        if line.find("X-DSPAM-Confidence") == -1: #means did not find
            continue
        else:
            index = line.find(":")+1
            spam_confidence.append(line[index:-1])
    for x in spam_confidence:
        spam_confidence_float.append(float(x))
    print(spam_confidence)
    print(spam_confidence_float)
    average_scf = sum(spam_confidence_float)/len(spam_confidence_float)
    print (average_scf)
except:
    print("bad file name")
    

